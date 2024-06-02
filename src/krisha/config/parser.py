import logging
from dataclasses import dataclass, field

import krisha.common.msg as msg

logger = logging.getLogger()


def default_user_agent():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36"
    }


def get_cities_url_map():
    return {
        0: "",
        1: "almaty/",
        2: "astana/",
        3: "shymkent/",
        4: "abay-oblast/",
        5: "akmolinskaja-oblast/",
        6: "aktjubinskaja-oblast/",
        7: "almatinskaja-oblast/",
        8: "atyrauskaja-oblast/",
        9: "vostochno-kazahstanskaja-oblast/",
        10: "zhambylskaja-oblast/",
        11: "jetisyskaya-oblast/",
        12: "zapadno-kazahstanskaja-oblast/",
        13: "karagandinskaja-oblast/",
        14: "kostanajskaja-oblast/",
        15: "kyzylordinskaja-oblast/",
        16: "mangistauskaja-oblast/",
        17: "pavlodarskaja-oblast/",
        18: "severo-kazahstanskaja-oblast/",
        19: "juzhno-kazahstanskaja-oblast/",
        20: "ulitayskay-oblast/",
    }


@dataclass(frozen=True)
class ParserConfig:
    """Parser configuration."""

    user_agent: dict = field(default_factory=default_user_agent)
    ads_on_page: int = 20
    sleep_time: int = 2
    max_skip_ad: int = 5
    retry_delay: tuple = (15, 60, 300, 1200, 3600)
    min_price: int = 0
    min_rooms: int = 0
    max_rooms: int = 5
    home_url: str = "https://krisha.kz"
    rent_url: str = "https://krisha.kz/arenda/kvartiry/"
    sep: str = "&das"
    q_pref: str = "?das"
    equ: str = "="
    br_equ: str = "[]="
    has_photo_url: str = "[_sys.hasphoto]=1"
    furniture_url: str = "[live.furniture]=1"
    rooms_url: str = "[live.rooms]"
    prices_from_url: str = "[price][from]="
    prices_to_url: str = "[price][to]="
    owner_url: str = "[who]=1"
    cities_url_map: dict = field(default_factory=get_cities_url_map)


def get_parser_config() -> ParserConfig:
    logger.info(msg.LOAD_PARSER_CONFIG_OK)
    return ParserConfig()
