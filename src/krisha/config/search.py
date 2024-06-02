import json
import logging
from dataclasses import dataclass
from json import JSONDecodeError
from typing import Any

import krisha.common.msg as msg

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

    city: int = 0
    has_photo: bool = False
    furniture: bool = False
    rooms: list | None = None
    price_from: int | None = None
    price_to: int | None = None
    owner: bool = False

    def __post_init__(self) -> None:
        self.city = self._validate_city(self.city)
        self.has_photo = self._validate_bool_args(self.has_photo, "has_photo")
        self.furniture = self._validate_bool_args(self.furniture, "furniture")
        self.rooms = self._validate_rooms(self.rooms)
        self.price_from = self._validate_price(self.price_from, "price_from")
        self.price_to = self._validate_price(self.price_to, "price_to")
        self.owner = self._validate_bool_args(self.owner, "owner")

    @staticmethod
    def _validate_city(city) -> int:
        if type(city) is int and 0 <= city < 21:
            return city
        logger.warning(msg.CR_CITY_VALIDATE.format(type(city), 0))
        return 0

    @staticmethod
    def _validate_bool_args(value: Any, name: str) -> bool:
        if not isinstance(value, bool):
            logger.warning(
                msg.CR_BOOL_VALIDATE.format(f"{name}", type(value), False)
            )
            return False
        return value

    @staticmethod
    def _validate_price(value: Any, name: str) -> int | None:
        if value is None:
            return
        if type(value) is int and value >= 0:
            return value
        logger.warning(msg.CR_GET_PRICE_URL.format(name, type(value), None))
        return

    @staticmethod
    def _validate_rooms(rooms) -> list | None:
        if rooms is None:
            return None
        if not isinstance(rooms, list) or len(rooms) == 0:
            logger.warning(msg.CR_GET_ROOMS_URL.format(type(rooms), None))
            return None
        valid_rooms = sorted(
            i for i in rooms if isinstance(i, int) and 0 < i < 6
        )
        return valid_rooms if valid_rooms else None


def get_search_parameters(file_name: str) -> SearchParameters:
    try:
        with open(file_name) as file:
            search_params = SearchParameters(**json.load(file))
            logger.info(msg.LOAD_SEARCH_PARAMS_OK)
            return search_params
    except (OSError, TypeError, JSONDecodeError) as error:
        logger.warning(msg.LOAD_SEARCH_PARAMS_ERROR.format(error))
    return SearchParameters()
