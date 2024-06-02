first_page_test_data = [
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/"
            "?das[_sys.hasphoto]=1"
            "&das[live.furniture]=1"
            "&das[live.rooms]=2"
            "&das[price][from]=150000"
            "&das[price][to]=500000"
            "&das[who]=1"
        ),
        "params": {
            "city": 0,
            "has_photo": True,
            "furniture": True,
            "rooms": [2],
            "price_from": 150000,
            "price_to": 500000,
            "owner": True,
        },
    },
    {
        "expected_url": "https://krisha.kz/arenda/kvartiry/",
        "params": {},
    },
    {
        "expected_url": "https://krisha.kz/arenda/kvartiry/almaty/",
        "params": {
            "city": 1,
            "rooms": 0,
        },
    },
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/almaty/"
            "?das[live.rooms]=1"
            "&das[price][to]=300000"
        ),
        "params": {
            "city": 1,
            "rooms": [1],
            "price_to": 300000,
        },
    },
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/almaty/"
            "?das[_sys.hasphoto]=1"
            "&das[live.rooms]=2"
            "&das[price][from]=100000"
            "&das[who]=1"
        ),
        "params": {
            "city": 1,
            "has_photo": True,
            "rooms": [2],
            "price_from": 100000,
            "owner": True,
        },
    },
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/astana/"
            "?das[_sys.hasphoto]=1"
            "&das[live.furniture]=1"
            "&das[live.rooms]=3"
            "&das[price][from]=300000"
            "&das[price][to]=500000"
        ),
        "params": {
            "city": 2,
            "has_photo": True,
            "furniture": True,
            "rooms": [3],
            "price_from": 300000,
            "price_to": 500000,
        },
    },
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/shymkent/"
            "?das[_sys.hasphoto]=1"
            "&das[live.furniture]=1"
            "&das[price][from]=100"
            "&das[price][to]=0"
        ),
        "params": {
            "city": 3,
            "has_photo": True,
            "furniture": True,
            "rooms": [0],
            "price_from": 100,
            "price_to": 0,
        },
    },
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/shymkent/"
            "?das[live.rooms]=4"
            "&das[price][from]=400000"
            "&das[price][to]=100000"
        ),
        "params": {
            "city": 3,
            "has_photo": "TEST_NON_PHOTO",
            "furniture": "TEST_NON_FURNITURE",
            "rooms": [4, 10, "TEST"],
            "price_from": 400000,
            "price_to": 100000,
            "owner": False,
        },
    },
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/astana/"
            "?das[live.rooms][]=2"
            "&das[live.rooms][]=5.100"
            "&das[price][from]=0"
            "&das[price][to]=0"
            "&das[who]=1"
        ),
        "params": {
            "city": 2,
            "has_photo": False,
            "furniture": False,
            "rooms": [10, 2, 1.2, 5, "TEST", True],
            "price_from": 0,
            "price_to": 0,
            "owner": True,
        },
    },
    {
        "expected_url": (
            "https://krisha.kz/arenda/kvartiry/almaty/"
            "?das[live.furniture]=1"
            "&das[price][from]=0"
            "&das[price][to]=0"
            "&das[who]=1"
        ),
        "params": {
            "city": 1,
            "has_photo": False,
            "furniture": True,
            "rooms": [-2, "TEST"],
            "price_from": 0,
            "price_to": 0,
            "owner": True,
        },
    },
]
