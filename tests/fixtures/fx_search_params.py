search_params_test_data = [
    (
        {
            "city": 0,
            "has_photo": False,
            "furniture": False,
            "rooms": None,
            "price_from": None,
            "price_to": None,
            "owner": False,
        },
        {},
    ),
    (
        {
            "city": 0,
            "has_photo": False,
            "furniture": False,
            "rooms": None,
            "price_from": 0,
            "price_to": None,
            "owner": False,
        },
        {
            "city": 21,
            "price_from": 0,
            "price_to": -123,
        },
    ),
    (
        {
            "city": 1,
            "has_photo": True,
            "furniture": True,
            "rooms": [1, 2],
            "price_from": 10000,
            "price_to": 50000,
            "owner": True,
        },
        {
            "city": 1,
            "has_photo": True,
            "furniture": True,
            "rooms": [1, 2],
            "price_from": 10000,
            "price_to": 50000,
            "owner": True,
        },
    ),
    (
        {
            "city": 0,
            "has_photo": False,
            "furniture": False,
            "rooms": None,
            "price_from": None,
            "price_to": None,
            "owner": False,
        },
        {
            "city": -1,
            "has_photo": "invalid",
            "furniture": "invalid",
            "rooms": [0, 6, "Test"],
            "price_from": -10000,
            "price_to": "invalid",
            "owner": "invalid",
        },
    ),
    (
        {
            "city": 0,
            "has_photo": False,
            "furniture": False,
            "rooms": None,
            "price_from": None,
            "price_to": None,
            "owner": False,
        },
        {
            "city": True,
            "rooms": (1, 2),
            "price_from": True,
        },
    ),
    (
        {
            "city": 0,
            "has_photo": False,
            "furniture": False,
            "rooms": None,
            "price_from": None,
            "price_to": None,
            "owner": False,
        },
        {
            "city": "Test",
            "rooms": 0,
            "owner": -500,
        },
    ),
]
