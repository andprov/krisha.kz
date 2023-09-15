# LOAD SEARCH PARAMETERS
READ_SEARCH_PARAMS_ERROR = (
    "Crawler - File with search parameters not found, use basic parameters {}"
)

# DB
DB_CREATED = "Database - CREATED OK"
DB_OK = "Database - CHECK OK"
DB_INSERT_OK = (
    "Database - Ads data has been successfully inserted into database"
)

# REQUEST
REQUEST_START = "Request - GET {}"
REQUEST_ERROR = "Request - GET {} - {}"
REQUEST_ERRORS_MAXIMUM = (
    "Request - Maximum number of retry attempts to execute request has been "
    "exceeded"
)

# RESPONSE
RESPONSE = "Response - Status code {}"

# CRAWLER
CR_START = "Crawler - START"
CR_STOPPED = "Crawler - STOPPED"
CR_FOUND = "Crawler - Search query has found {} advertisements across {} pages"
CR_ADS_NOT_FOUND = (
    "Crawler - STOPPED: Ads not found. Try using other search parameters"
)
CR_PROCESS = "Crawler - Processed {} pages out of {}"
CR_FLAT_DATA_OK = "Crawler - Flat data is obtained from Ad"
CR_ADS_ON_PAGE_OK = "Crawler - Ads data on page has been processed"
CR_NEXT_PAGE_OK = "Crawler - Next page url found"
CR_SKIP_AD = "Crawler - Ad will be skipped due to unavailability of page"
CR_SLEEP = "Crawler - Sleep {} seconds"
CR_MISSED_MAXIMUM = (
    "Crawler - Maximum number of skipped Ads has been exceeded. "
    "Check correctness of Ad URL formation"
)
CR_SOUP_FIND_ERROR = "Crawler - Soup data < {} > not found"
CR_JS_PARS_ERROR = "Crawler - Unable to find JS script"
CR_JSON_ERROR = "Crawler - Json load error: {}"
CR_KEY_DATA_ERROR = (
    "Crawler - Key < {} > not found, "
    "or data type for key does not match expected type, "
    "or collection contains empty data"
)
CR_KEY_GET_ERROR = "Crawler - Key < {} > in JS not found"
CR_NON_VALID_FLATS_DATA = (
    "Crawler - Flats_data list does not contain instances of Flat "
    "class. "
    "Please check methods of Flat class responsible for searching data "
    "on Ad page"
)
CR_CITY_VALIDATE = (
    "Crawler - Parameter 'city' contains unavailable data: < {} >. "
    "An integer from 0 to 20 is required. "
    "Default value < {} > will be used"
)
CR_BOOL_VALIDATE = (
    "Crawler - Parameter contains unavailable data {}. "
    "Value must be True or False. "
    "Default value < {} > will be used"
)
CR_GET_ROOMS_URL = (
    "Crawler - Parameter 'rooms' contains unavailable data < {} >. "
    "Available format is a <tuple> with no more than five "
    "elements, where each element is a positive integer "
    "from 1 to 5. "
    "Default value < {} > will be used"
)
CR_GET_PRICE_URL = (
    "Crawler - Parameter 'price' contains unavailable data < {} >. "
    "Available price value is a positive integer from 0 to 1000000. "
    "Default price value < {} > will be used"
)
