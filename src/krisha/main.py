import logging
import sys

from krisha.config.config import load_config
from krisha.crawler.first_page import FirstPage
from krisha.crawler.spider import run_crawler
from krisha.db.service import get_connection

logger = logging.getLogger()


def main():
    config = load_config()
    connector = get_connection(config.path.db_file)
    first_page_url = FirstPage.get_url(config)
    run_crawler(config, connector, first_page_url)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logger.critical(msg=error, exc_info=True)
        sys.exit()
