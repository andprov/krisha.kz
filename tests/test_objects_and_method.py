import logging
from unittest import TestCase

from bs4 import BeautifulSoup as bs
from krisha.crawler.first_page import FirstPage
from krisha.crawler.flat import Flat

from tests.fixtures.fx_first_page import first_page_test_data
from tests.fixtures.fx_flat import expected_data, valid_script

logging.getLogger().disabled = True


class TestFirstPage(TestCase):
    def test_first_page_url(self):
        for name, expected_url, params in first_page_test_data:
            with self.subTest():
                url = FirstPage().get_url(**params)
                self.assertEqual(
                    expected_url,
                    url,
                    msg=(
                        f"Generated address of the page "
                        f"< {name} > "
                        f"does not match the expected one"
                    ),
                )


class TestFlat(TestCase):
    def test_from_ad_valid_content(self):
        content = bs(valid_script, "html.parser")
        url = expected_data["url"]
        flat = Flat.from_ad(content, url)
        for key, value in flat.__dict__.items():
            with self.subTest():
                self.assertEqual(
                    expected_data[key],
                    value,
                    msg="Attribute value does not match the expected value",
                )
