# DB
DB_CREATED = "Database - CREATED OK"
DB_OK = "Database - CHECK OK"
DB_INSERT_OK = (
    "Database - Ads data has been successfully inserted into database"
)

# REQUEST
REQUEST_START = "Request - GET {}"
REQUEST_ERROR = "Request - GET {} - {}"

# RESPONSE
RESPONSE = "Response - Status code {}"

# CRAWLER
CR_LOGGER_CONFIG_OK = "Crawler - Logging configured successfully"
CR_LOGGER_CONFIG_WRONG = (
    "logging config file not found, use basic config.\n    ERROR: {}"
)
LOAD_PARSER_CONFIG_OK = "Crawler - Load parser config OK"
LOAD_SEARCH_PARAMS_ERROR = (
    "Crawler - Load search parameters ERROR. Use basic parameters. "
    "\n     ERROR: {}"
)
LOAD_SEARCH_PARAMS_OK = "Crawler - Load search parameters OK"
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
CR_SOUP_FIND_ERROR = "Crawler - Soup data < {} > not found"
CR_JS_PARS_ERROR = "Crawler - Unable to find JS script"
CR_JSON_ERROR = "Crawler - Json load error: \n      ERROR: {}"
CR_KEY_DATA_ERROR = (
    "Crawler - Key < {} > not found, "
    "or data type for key does not match expected type, "
    "or collection contains empty data"
)
CR_KEY_GET_ERROR = "Crawler - Key < {} > in JS not found"
CR_CITY_VALIDATE = (
    "Crawler - Parameter 'city' contains unavailable: {}. "
    "An integer from 0 to 20 is required. "
    "Default value < {} > will be used"
)
CR_BOOL_VALIDATE = (
    "Crawler - Parameter {} contains unavailable type: {}. "
    "Value must be True or False. "
    "Default value < {} > will be used"
)
CR_GET_ROOMS_URL = (
    "Crawler - Parameter 'rooms' contains unavailable type: {}. "
    "Available format is a <list> with no more than five elements, "
    "where each element is a positive integer from 1 to 5. "
    "Default value < {} > will be used"
)
CR_GET_PRICE_URL = (
    "Crawler - Parameter {} contains unavailable type: {}. "
    "Available price value is a positive integer from 0 to 1000000. "
    "Default price value < {} > will be used"
)
