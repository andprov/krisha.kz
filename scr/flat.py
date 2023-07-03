import logging
import json

import scr.misc.msg as msg


logger = logging.getLogger()


class Flat:
    """Flat object."""

    def __init__(self):
        self.id = None
        self.uuid = None
        self.url = None
        self.room = None
        self.square = None
        self.city = None
        self.lat = None
        self.lon = None
        self.description = None
        self.photo = None
        self.price = None
        self.star = None
        self.focus = None

    def from_db(self):
        """Create Flat object from DB."""
        pass

    @classmethod
    def from_ad(cls, content, url):
        """Create Flat object from Ad."""
        flat = cls()
        pars_data = cls._get_pars_data(content)
        advert = cls._get_advert(pars_data, "advert")
        adverts = cls._get_adverts(pars_data, "adverts")
        flat.id = cls._get_sub_data(advert, "id", required=True)
        flat.uuid = cls._get_sub_data(adverts, "uuid", required=True)
        flat.url = url
        flat.room = cls._get_sub_data(advert, "rooms")
        flat.square = cls._get_sub_data(advert, "square")
        address = cls._get_sub_data(adverts, "fullAddress")
        flat.city = address.split(",")[0] if address else None
        lat_lon = cls._get_sub_data(advert, "map")
        flat.lat = cls._get_sub_data(lat_lon, "lat") if lat_lon else None
        flat.lon = cls._get_sub_data(lat_lon, "lon") if lat_lon else None
        flat.description = cls._get_sub_data(adverts, "description")
        photos = cls._get_sub_data(advert, "photos")
        flat.photo = cls._get_sub_data(photos[0], "src") if photos else None
        flat.price = cls._get_sub_data(advert, "price", required=True)
        return flat

    @staticmethod
    def _get_pars_data(content):
        script = content.find("script", id="jsdata")
        if not script:
            raise ValueError(msg.CR_SOUP_FIND_ERROR.format("jsdata"))
        string = script.text.strip()
        start_index = string.find("{")
        end_ndex = string.rfind("}")
        if start_index == -1 or end_ndex == -1:
            raise ValueError(msg.CR_JS_PARS_ERROR)
        json_string = string[start_index:end_ndex + 1]
        try:
            data = json.loads(json_string)
            return data
        except Exception as error:
            raise ValueError(msg.CR_JSON_ERROR.format(error))

    @staticmethod
    def _get_advert(pars_data, key):
        advert = pars_data.get(key)
        if not isinstance(advert, dict) or not advert:
            raise ValueError(msg.CR_KEY_DATA_ERROR.format(key))
        return advert

    @staticmethod
    def _get_adverts(pars_data, key):
        adverts = pars_data.get(key)
        if (
            not isinstance(adverts, list)
            or not adverts
            or not isinstance(adverts[0], dict)
            or not adverts[0]
        ):
            raise ValueError(msg.CR_KEY_DATA_ERROR.format(key))
        return adverts[0]

    @staticmethod
    def _get_sub_data(data, key, required=False):
        sub_data = data.get(key)
        if not sub_data:
            if required:
                raise ValueError(msg.CR_KEY_GET_ERROR.format(key))
            logger.warning(msg.CR_KEY_GET_ERROR.format(key))
        return sub_data
