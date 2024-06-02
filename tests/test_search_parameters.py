import pytest

from krisha.config.app_config import load_config
from krisha.config.search import SearchParameters
from tests.fixtures.fx_search_params import search_params_test_data


@pytest.mark.parametrize("expected_data, params", search_params_test_data)
def test_search_parameters_data(expected_data, params):
    config = load_config()
    search_params = SearchParameters(config.parser_config, **params)

    assert search_params.city == expected_data["city"]
    assert search_params.has_photo == expected_data["has_photo"]
    assert search_params.furniture == expected_data["furniture"]
    assert search_params.rooms == expected_data["rooms"]
    assert search_params.price_from == expected_data["price_from"]
    assert search_params.price_to == expected_data["price_to"]
    assert search_params.owner == expected_data["owner"]
