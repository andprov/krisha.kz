# config_vars
USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
SEAR_PARAMS_FILE = "SEARCH_PARAMETERS.json"
ADS_ON_PAGE = 20
PRICE_MAX = 1000001
SLEEP_TIME = 2
MAX_SKIP_AD = 5
RETRY_DELAY = (15, 60, 300, 1200, 3600)
DEFAULT_CITY = 0

# url
HOME_URL = "https://krisha.kz"
RENT_URL = "https://krisha.kz/arenda/kvartiry/"
SEP = "&das"
DEL = "?das"
EQU = "="
BR_EQU = "[]="
CITIES_URL = {
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
HAS_PHOTO_URL = "[_sys.hasphoto]=1"
FURNITURE_URL = "[live.furniture]=1"
ROOMS_URL = "[live.rooms]"
PRICES_FROM_URL = "[price][from]="
PRICES_TO_URL = "[price][to]="
OWNER_URL = "[who]=1"

# db
DB_PATH = "db.sqlite"
