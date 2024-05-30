from krisha.config.search import SearchParameters


def test_default_parameters():
    search_params = SearchParameters()
    assert search_params.city == 0
    assert not search_params.has_photo
    assert not search_params.furniture
    assert search_params.rooms is None
    assert search_params.price_from is None
    assert search_params.price_to is None
    assert not search_params.owner


def test_valid_parameters():
    valid_params = {
        "city": 1,
        "has_photo": True,
        "furniture": True,
        "rooms": [1, 2],
        "price_from": 10000,
        "price_to": 50000,
        "owner": False,
    }
    search_params = SearchParameters(**valid_params)
    assert search_params.city == valid_params["city"]
    assert search_params.has_photo
    assert search_params.furniture
    assert search_params.rooms == valid_params["rooms"]
    assert search_params.price_from == valid_params["price_from"]
    assert search_params.price_to == valid_params["price_to"]
    assert not search_params.owner


def test_invalid_parameters():
    invalid_params = {
        "city": -1,
        "has_photo": "invalid",
        "furniture": "invalid",
        "rooms": [0, 6],
        "price_from": -10000,
        "price_to": "invalid",
        "owner": "invalid",
    }
    search_params = SearchParameters(**invalid_params)
    assert search_params.city == 0
    assert not search_params.has_photo
    assert not search_params.furniture
    assert search_params.rooms is None
    assert search_params.price_from is None
    assert search_params.price_to is None
    assert not search_params.owner
