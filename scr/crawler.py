import logging
import re
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup as bs, ResultSet
from requests import Response
from tqdm import trange
from tqdm.contrib.logging import logging_redirect_tqdm

import scr.config as cfg
import scr.misc.msg as msg
from db.queries import insert_flats_data_db
from scr.flat import Flat
from scr.misc.exceptions import MissedAdMaximum, RequestErrorsMaximum

logger = logging.getLogger()


def get_response(url: str) -> Response:
    for delay in cfg.RETRY_DELAY:
        logger.debug(msg.REQUEST_START.format(url))
        try:
            response: Response = requests.get(
                url, headers=cfg.USER_AGENT, timeout=20
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

    raise RequestErrorsMaximum(msg.REQUEST_ERRORS_MAXIMUM)


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


def get_page_count(content: bs, ads_count: int) -> int:
    page_count = 1
    if ads_count > cfg.ADS_ON_PAGE:
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
    ads: ResultSet = ads_section.find_all("div", attrs={"data-id": True})
    if not ads:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("data-id"))
    return ads


def get_ads_urls(ads_on_page: ResultSet) -> list[str]:
    ads_urls = []
    for ad in ads_on_page:
        title = ad.find("a", class_="a-card__title")
        if not title:
            raise ValueError(msg.CR_SOUP_FIND_ERROR.format("a-card__title"))
        ad_url = title.get("href")
        if not ad_url:
            raise ValueError(msg.CR_SOUP_FIND_ERROR.format("href"))
        ads_urls.append(cfg.HOME_URL + ad_url)
    return ads_urls


def get_flats_data_on_page(ads_urls: list[str]) -> list[Flat | None]:
    missed_ad_counter: int = 0
    flats_data: list = []
    for url in ads_urls:
        try:
            response: Response = get_response(url)
        except RequestErrorsMaximum:
            missed_ad_counter += 1
            if missed_ad_counter > cfg.MAX_SKIP_AD:
                raise MissedAdMaximum(msg.CR_MISSED_MAXIMUM)
            logger.warning(msg.CR_SKIP_AD)
        else:
            content: bs = get_content(response)
            flats_data.append(Flat.from_ad(content, url))
            logger.debug(msg.CR_FLAT_DATA_OK)

        sleep(cfg.SLEEP_TIME)

    logger.debug(msg.CR_ADS_ON_PAGE_OK)
    return flats_data


def validate_flats_data(flats_data: list[Flat | None]) -> list[Flat]:
    validated_data: list[Flat] = [i for i in flats_data if i is not None]
    if not validated_data:
        raise ValueError(msg.CR_NON_VALID_FLATS_DATA)
    return validated_data


def get_next_url(content: bs) -> str:
    next_btn = content.find("a", class_="paginator__btn--next")
    if not next_btn:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("paginator__btn--next"))
    next_btn_url = next_btn.get("href")
    if not next_btn_url:
        raise ValueError(msg.CR_SOUP_FIND_ERROR.format("href"))
    url: str = cfg.HOME_URL + next_btn_url
    logger.debug(msg.CR_NEXT_PAGE_OK)
    return url


def run_crawler(url: str) -> None:
    response: Response = get_response(url)
    content: bs = get_content(response)
    ads_count: int = get_ads_count(content)
    page_count: int = get_page_count(content, ads_count)

    with logging_redirect_tqdm():
        for num in trange(1, page_count + 1):
            ads_on_page: ResultSet = get_ads_on_page(content)
            ads_urls: list[str] = get_ads_urls(ads_on_page)
            flats_data: list[Flat | None] = get_flats_data_on_page(ads_urls)
            validated_data: list[Flat] = validate_flats_data(flats_data)
            insert_flats_data_db(validated_data)
            logger.info(msg.CR_PROCESS.format(num, page_count))

            sleep(cfg.SLEEP_TIME)

            if num < page_count:
                next_url: str = get_next_url(content)
                response: Response = get_response(next_url)
                content: bs = get_content(response)

    logger.info(msg.CR_STOPPED)
