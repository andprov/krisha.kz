import pytest

from tests.fixtures.fx_first_page import first_page_test_data
from krisha.config.app_config import load_config
from krisha.config.search import SearchParameters
from krisha.crawler.first_page import FirstPage


@pytest.mark.parametrize("expected_url, params", first_page_test_data)
def test_first_page_url_created(expected_url, params):
    config = load_config()
    config.search_params = SearchParameters(**params)
    url = FirstPage.get_url(config)

    assert url == expected_url
