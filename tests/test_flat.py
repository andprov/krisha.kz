from bs4 import BeautifulSoup

from tests.fixtures.fx_flat import valid_script
from krisha.crawler.flat_parser import CreateFlat
from krisha.entities.flat import Flat


content = BeautifulSoup(valid_script, "html.parser")


def test_valid_data():
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
    flat = CreateFlat.get_flat(content, url)

    assert flat == expected_flat


def test_get_pars_data():
    pars_data = CreateFlat._get_pars_data(content)

    assert pars_data["advert"]["id"] == 680044731


def test_get_advert_data():
    pars_data = CreateFlat._get_pars_data(content)
    advert = CreateFlat._get_advert(pars_data, "advert")

    assert advert["id"] == 680044731


def test_get_adverts():
    pars_data = CreateFlat._get_pars_data(content)
    adverts = CreateFlat._get_adverts(pars_data, "adverts")

    assert adverts["uuid"] == "b7331c3a-3219-410a-a04c-47043a354dc7"


def test_get_sub_data():
    data = {"key1": "value1", "key2": "value2"}

    assert CreateFlat._get_sub_data(data, "key1") == "value1"
    assert CreateFlat._get_sub_data(data, "key3") is None
