import logging
import re

import scr.config as cfg
import scr.misc.msg as msg

logger = logging.getLogger()


class FirstPage:
    """First page URL based on the search parameters."""

    @classmethod
    def get_url(
        cls,
        city: int = 0,
        has_photo: bool = False,
        furniture: bool = False,
        rooms: list[int] = None,
        price_from: int = None,
        price_to: int = None,
        owner: bool = False,
    ):
        """Generate a URL using the provided data.

        Args:
            city (int): City code.
            has_photo (bool): Indicates if the listing should have photos.
            furniture (bool): Indicates if the listing should have furniture.
            rooms (list[int]): List of room numbers.
            price_from (int): Minimum price.
            price_to (int): Maximum price.
            owner (bool): Indicates if the listing from the owner.
        """
        city = cls._get_city_url(city)
        search_param = (
            cls._get_param_url(has_photo, cfg.HAS_PHOTO_URL),
            cls._get_param_url(furniture, cfg.FURNITURE_URL),
            cls._get_rooms_url(rooms),
            cls._get_price_url(price_from, cfg.PRICES_FROM_URL),
            cls._get_price_url(price_to, cfg.PRICES_TO_URL),
            cls._get_param_url(owner, cfg.OWNER_URL),
        )
        url = cls._concatenate_params(city, search_param)
        return url

    @staticmethod
    def _get_city_url(city):
        """Check value for city selection and return string with city url."""
        if not isinstance(city, int) or not (0 <= city < 21):
            logger.warning(msg.CR_CITY_VALIDATE.format(city, cfg.DEFAULT_CITY))
            return cfg.CITIES_URL[cfg.DEFAULT_CITY]
        return cfg.CITIES_URL[city]

    @staticmethod
    def _get_param_url(arg, url):
        """Check data and return string with parameters url or None."""
        if not isinstance(arg, bool):
            logger.warning(msg.CR_BOOL_VALIDATE.format(type(arg), False))
            return
        if arg:
            return url

    @staticmethod
    def _get_rooms_url(arg):
        """Check data and return string with rooms url or None."""
        if arg is None:
            return
        if not isinstance(arg, list) or len(arg) > 5:
            logger.warning(msg.CR_GET_ROOMS_URL.format(arg, None))
            return
        rooms = [i for i in arg if isinstance(i, int) and 0 < i < 6]
        if len(rooms) == 1:
            return cfg.EQU.join([cfg.ROOMS_URL, str(*rooms)])
        if len(rooms) > 1:
            rooms = sorted(rooms)
            room_data = [
                cfg.BR_EQU.join([cfg.ROOMS_URL, str(i)]) for i in rooms
            ]
            return re.sub(r"\b5\b", "5.100", cfg.SEP.join(room_data))

    @staticmethod
    def _get_price_url(price, url):
        """Check data and return string with price url or None."""
        if price is None:
            return
        if not isinstance(price, int) or not (0 <= price < cfg.PRICE_MAX):
            logger.warning(msg.CR_GET_PRICE_URL.format(price, None))
            return
        return f"{url}{price}"

    @staticmethod
    def _concatenate_params(city, search_param):
        """Concatenate parameters in to URL."""
        full_url = cfg.RENT_URL + city
        search_str = cfg.SEP.join(i for i in search_param if i is not None)
        if search_str:
            full_url += cfg.DEL + search_str
        return full_url
