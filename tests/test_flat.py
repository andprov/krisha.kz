from bs4 import BeautifulSoup

from krisha.crawler.flat_parser import FlatParser
from krisha.entities.flat import Flat
from tests.fixtures.fx_flat import valid_script

CONTENT = BeautifulSoup(valid_script, "html.parser")


def test_flat_valid_data():
    expected_flat = Flat(
        id=680044731,
        uuid="b7331c3a-3219-410a-a04c-47043a354dc7",
        url="https://krisha.kz/a/show/680044731",
        room=1,
        square=30,
        city="Алматы",
        lat=43.260625,
        lon=76.962848,
        description="Номер в Апарт-гостинице City Park!",
        photo="https://cf-kr.kcdn.online/webp/b7/1-full.jpg",
        price=300000,
        star=None,
        focus=None,
    )
    url = "https://krisha.kz/a/show/680044731"
    flat = FlatParser.get_flat(CONTENT, url)

    assert flat == expected_flat


def test_get_pars_data():
    pars_data = FlatParser._get_pars_data(CONTENT)

    assert pars_data["advert"]["id"] == 680044731
    assert pars_data["adverts"] == [
        {
            "description": "Номер в Апарт-гостинице City Park!",
            "fullAddress": "Алматы, Наурызбайский р-н, Жунисова",
            "uuid": "b7331c3a-3219-410a-a04c-47043a354dc7",
        }
    ]


def test_get_advert_data():
    pars_data = FlatParser._get_pars_data(CONTENT)
    advert = FlatParser._get_advert(pars_data, "advert")

    assert advert["id"] == 680044731
    assert advert["map"] == {"lat": 43.260625, "lon": 76.962848}
    assert advert["photos"] == [
        {
            "src": "https://cf-kr.kcdn.online/webp/b7/1-full.jpg",
            "title": "Аренда квартир в Алматы: 1-комнатная ",
        }
    ]
    assert advert["price"] == 300000
    assert advert["rooms"] == 1
    assert advert["square"] == 30


def test_get_adverts():
    pars_data = FlatParser._get_pars_data(CONTENT)
    adverts = FlatParser._get_adverts(pars_data, "adverts")

    assert adverts["uuid"] == "b7331c3a-3219-410a-a04c-47043a354dc7"
    assert adverts["fullAddress"] == "Алматы, Наурызбайский р-н, Жунисова"
    assert adverts["description"] == "Номер в Апарт-гостинице City Park!"


def test_get_sub_data():
    data = {"key1": "value1", "key2": "value2"}

    assert FlatParser._get_sub_data(data, "key1") == "value1"
    assert FlatParser._get_sub_data(data, "key3") is None
