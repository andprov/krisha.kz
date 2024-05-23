import json
import logging
from dataclasses import dataclass
from json import JSONDecodeError
from typing import Any

import krisha.common.msg as msg
from krisha.config.models.base import BaseConfigModel

logger = logging.getLogger()


@dataclass
class SearchParameters(BaseConfigModel):
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

    def _validate(self) -> None:
        self._validate_city()
        self._validate_has_photo()
        self._validate_furniture()
        self._validate_rooms()
        self._validate_price_from()
        self._validate_price_to()

    @staticmethod
    def _validate_bool_args(name: str, value: Any) -> bool:
        if not isinstance(value, bool):
            logger.warning(
                msg.CR_BOOL_VALIDATE.format(f"{name}", type(value), False)
            )
            return False
        return value

    @staticmethod
    def _validate_price_args(name: str, value: Any) -> int | None:
        if value is None:
            return None
        if not isinstance(value, int) or value < 0:
            logger.warning(
                msg.CR_GET_PRICE_URL.format(name, type(value), None)
            )
            return None
        return value

    def _validate_city(self) -> None:
        if not isinstance(self.city, int) or not 0 <= self.city < 21:
            logger.warning(msg.CR_CITY_VALIDATE.format(type(self.city), 0))
            self.city = 0

    def _validate_has_photo(self) -> None:
        self.has_photo = self._validate_bool_args(
            "< has_photo >", self.has_photo
        )

    def _validate_furniture(self) -> None:
        self.furniture = self._validate_bool_args(
            "< furniture >", self.furniture
        )

    def _validate_rooms(self) -> None:
        if self.rooms is None:
            return
        if not isinstance(self.rooms, list) or len(self.rooms) == 0:
            logger.warning(msg.CR_GET_ROOMS_URL.format(type(self.rooms), None))
            self.rooms = None
            return
        rooms = {i for i in self.rooms if isinstance(i, int) and 0 < i < 6}
        if len(rooms) > 1:
            rooms = sorted(rooms)
        self.rooms = rooms

    def _validate_price_from(self) -> None:
        self.price_from = self._validate_price_args(
            "< price_from >", self.price_from
        )

    def _validate_price_to(self) -> None:
        self.price_to = self._validate_price_args(
            "< price_to >", self.price_to
        )


def get_search_parameters(file_name: str) -> SearchParameters:
    try:
        with open(file_name) as file:
            search_params = SearchParameters(**json.load(file))
            logger.info(msg.LOAD_SEARCH_PARAMS_OK)
            return search_params
    except (OSError, TypeError, JSONDecodeError) as error:
        logger.warning(msg.LOAD_SEARCH_PARAMS_ERROR.format(error))
    return SearchParameters()
