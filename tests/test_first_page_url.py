from tests.fixtures.fx_first_page import first_page_test_data
from krisha.config.app_config import load_config
from krisha.config.search import SearchParameters
from krisha.crawler.first_page import FirstPage


def test_first_page_url_created():
    config = load_config()
    for fixture in first_page_test_data:
        config.search_params = SearchParameters(**fixture["params"])
        url = FirstPage.get_url(config)

        assert url == fixture["expected_url"]
