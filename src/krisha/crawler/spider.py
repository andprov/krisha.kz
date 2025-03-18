import logging
import re
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup as bs
from bs4 import ResultSet
from requests import Response
from tqdm import trange
from tqdm.contrib.logging import logging_redirect_tqdm

import krisha.common.msg as msg
from krisha.config import Config
from krisha.crawler.flat_parser import FlatParser
from krisha.db.base import DBConnection
from krisha.db.queries import insert_flats_data_db
from krisha.entities.flat import Flat
from krisha.exceptions.crawler import (
    MaximumMissedAdError,
    MaximumRetryRequestsError,
)

logger = logging.getLogger()


def get_response(url: str, config: Config) -> Response:
    for delay in config.parser_config.retry_delay:
        logger.debug(msg.REQUEST_START.format(url))
        try:
            response = requests.get(
                url,
                headers=config.parser_config.user_agent,
                timeout=config.parser_config.timeout,
            )
            response.raise_for_status()
            if response.status_code == requests.codes.ok:
                logger.debug(msg.RESPONSE.format(response.status_code, url))
                return response
            logger.error(msg.RESPONSE.format(response.status_code))
        except requests.RequestException as error:
            logger.error(msg.REQUEST_ERROR.format(url, error))
            logger.debug(msg.CR_SLEEP.format(delay))

            sleep(delay)

    raise MaximumRetryRequestsError


def get_content(response: Response) -> bs:
    return bs(response.text, "html.parser")


def get_ads_count(content: bs) -> int:
    if not content.find("div", class_="a-search-options"):
        logger.warning(msg.CR_ADS_NOT_FOUND)
        sys.exit()
    logger.info(msg.CR_START)
    subtitle = content.find("div", class_="a-search-subtitle")
    if not subtitle:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("a-search-subtitle"))
    ads_count = int("".join(re.findall(r"\d+", subtitle.text.strip())))
    return ads_count


def get_page_count(content: bs, ads_count: int, config: Config) -> int:
    page_count = 1
    if ads_count > config.parser_config.ads_on_page:
        paginator = content.find("nav", class_="paginator")
        if not paginator:
            raise ValueError(msg.CR_SOUP_FIND_ERROR.format("paginator"))
        page_count = int(paginator.text.split()[-2])
    logger.info(msg.CR_FOUND.format(ads_count, page_count))
    return page_count


def get_ads_on_page(content: bs) -> ResultSet:
    ads_section = content.find("section", class_="a-search-list")
    if not ads_section:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("a-search-list"))
    ads = ads_section.find_all("div", attrs={"data-id": True})
    if not ads:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("data-id"))
    return ads


def get_ads_urls(home_url, ads_on_page: ResultSet) -> list[str]:
    ads_urls = []
    for ad in ads_on_page:
        title = ad.find("a", class_="a-card__title")
        if not title:
            raise ValueError(msg.CR_SOUP_FIND_ERROR.format("a-card__title"))
        ad_url = title.get("href")
        if not ad_url:
            raise ValueError(msg.CR_SOUP_FIND_ERROR.format("href"))
        ads_urls.append(home_url + ad_url)
    return ads_urls


def get_flats_data_on_page(
    ads_urls: list[str],
    config: Config,
    flat_parser: type[FlatParser],
) -> list[Flat]:
    missed_ad_counter = 0
    flats_data = []
    for url in ads_urls:
        try:
            response = get_response(url, config)
        except MaximumRetryRequestsError as error:
            missed_ad_counter += 1
            if missed_ad_counter > config.parser_config.max_skip_ad:
                raise MaximumMissedAdError from error
            logger.warning(msg.CR_SKIP_AD)
        else:
            content = get_content(response)
            flats_data.append(flat_parser.get_flat(content, url))
            logger.debug(msg.CR_FLAT_DATA_OK)

        sleep(config.parser_config.sleep_time)

    logger.debug(msg.CR_ADS_ON_PAGE_OK)
    return flats_data


def get_next_url(home_url, content: bs) -> str:
    next_btn = content.find("a", class_="paginator__btn--next")
    if not next_btn:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("paginator__btn--next"))
    next_btn_url = next_btn.get("href")
    if not next_btn_url:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("href"))
    url = home_url + next_btn_url
    logger.debug(msg.CR_NEXT_PAGE_OK)
    return url


def run_crawler(
    config: Config,
    connector: DBConnection,
    url: str,
    flat_parser: type[FlatParser],
) -> None:
    response = get_response(url, config)
    content = get_content(response)
    ads_count = get_ads_count(content)
    page_count = get_page_count(content, ads_count, config)

    with logging_redirect_tqdm():
        for num in trange(1, page_count + 1):
            ads_on_page = get_ads_on_page(content)
            ads_urls = get_ads_urls(config.parser_config.home_url, ads_on_page)
            flats_data = get_flats_data_on_page(ads_urls, config, flat_parser)
            insert_flats_data_db(connector, flats_data)
            logger.info(msg.CR_PROCESS.format(num, page_count))

            sleep(config.parser_config.sleep_time)

            if num < page_count:
                next_url = get_next_url(config.parser_config.home_url, content)
                response = get_response(next_url, config)
                content = get_content(response)

    logger.info(msg.CR_STOPPED)
