import logging
import re

from krisha.config import Config
from krisha.config.parser import ParserConfig

logger = logging.getLogger()


class FirstPage:
    """First page URL based on the search parameters."""

    @staticmethod
    def _get_param_url(arg: bool, url: str) -> str | None:
        return url if arg else None

    @staticmethod
    def _get_rooms_url(rooms: list | None, parser: ParserConfig) -> str | None:
        if rooms is None:
            return
        if len(rooms) == 1:
            return parser.equ.join([parser.rooms_url, str(*rooms)])
        room_data = [
            parser.br_equ.join([parser.rooms_url, str(i)]) for i in rooms
        ]
        return re.sub(r"\b5\b", "5.100", parser.sep.join(room_data))

    @staticmethod
    def _get_price_url(price: int | None, url: str) -> str | None:
        if price is None:
            return
        return f"{url}{price}"

    @staticmethod
    def _concatenate_params_url(
        parser: ParserConfig, city_url: str, param_urls: tuple
    ) -> str:
        full_url = parser.rent_url + city_url
        search_str = parser.sep.join(i for i in param_urls if i is not None)
        if search_str:
            full_url += parser.q_pref + search_str
        return full_url

    @classmethod
    def get_url(cls, config: Config) -> str:
        search = config.search_params
        parser = config.parser_config
        city_url = parser.cities_url_map.get(search.city)
        param_urls = (
            cls._get_param_url(search.has_photo, parser.has_photo_url),
            cls._get_param_url(search.furniture, parser.furniture_url),
            cls._get_rooms_url(search.rooms, parser),
            cls._get_price_url(search.price_from, parser.prices_from_url),
            cls._get_price_url(search.price_to, parser.prices_to_url),
            cls._get_param_url(search.owner, parser.owner_url),
        )
        return cls._concatenate_params_url(parser, city_url, param_urls)
