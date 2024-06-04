import json
import logging
from dataclasses import dataclass
from json import JSONDecodeError
from typing import Any

import krisha.common.msg as msg
from krisha.config.parser import ParserConfig

logger = logging.getLogger()


@dataclass
class SearchParameters:
    """Init and validate search parameters.

    Attributes:
        city: int = 0
        has_photo: bool = False
        furniture: bool = False
        rooms: tuple = None
        price_from: int = None
        price_to: int = None
        owner: bool = False
    """

    parser_config: ParserConfig
    city: int = 0
    has_photo: bool = False
    furniture: bool = False
    rooms: list | None = None
    price_from: int | None = None
    price_to: int | None = None
    owner: bool = False

    def __post_init__(self) -> None:
        self.city = self._validate_city(
            self.city,
            self.parser_config,
        )
        self.has_photo = self._validate_bool_args(
            self.has_photo,
            "has_photo",
        )
        self.furniture = self._validate_bool_args(
            self.furniture,
            "furniture",
        )
        self.rooms = self._validate_rooms(
            self.rooms,
            self.parser_config,
        )
        self.price_from = self._validate_price(
            self.price_from,
            "price_from",
            self.parser_config,
        )
        self.price_to = self._validate_price(
            self.price_to,
            "price_to",
            self.parser_config,
        )
        self.owner = self._validate_bool_args(
            self.owner,
            "owner",
        )

    @staticmethod
    def _validate_city(city, parser_config: ParserConfig) -> int:
        min_city_idx = min(parser_config.cities_url_map)
        max_city_idx = max(parser_config.cities_url_map)
        if type(city) is int and min_city_idx <= city <= max_city_idx:
            return city
        logger.warning(msg.CR_CITY_VALIDATE.format(type(city), min_city_idx))
        return min_city_idx

    @staticmethod
    def _validate_bool_args(value: Any, name: str) -> bool:
        if type(value) is bool:
            return value
        logger.warning(
            msg.CR_BOOL_VALIDATE.format(f"{name}", type(value), False)
        )
        return False

    @staticmethod
    def _validate_price(
        value: Any,
        name: str,
        parser_config: ParserConfig,
    ) -> int | None:
        if value is None:
            return
        if type(value) is int and value >= parser_config.min_price:
            return value
        logger.warning(msg.CR_GET_PRICE_URL.format(name, type(value), None))
        return

    @staticmethod
    def _validate_rooms(rooms, parser_config: ParserConfig) -> list | None:
        if rooms is None:
            return
        min_rooms = parser_config.min_rooms
        max_rooms = parser_config.max_rooms
        if type(rooms) is not list or len(rooms) == min_rooms:
            logger.warning(msg.CR_GET_ROOMS_URL.format(type(rooms), None))
            return
        valid_rooms = sorted(
            i for i in rooms if (type(i) is int and min_rooms < i <= max_rooms)
        )
        return valid_rooms if valid_rooms else None


def get_search_parameters(
    file_name: str,
    parser_config: ParserConfig,
) -> SearchParameters:
    try:
        with open(file_name) as file:
            search_params = SearchParameters(parser_config, **json.load(file))
            logger.info(msg.LOAD_SEARCH_PARAMS_OK)
            return search_params
    except (OSError, TypeError, JSONDecodeError) as error:
        logger.warning(msg.LOAD_SEARCH_PARAMS_ERROR.format(error))
    return SearchParameters(parser_config)
