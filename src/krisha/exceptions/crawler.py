from krisha.exceptions.base import CrawlerError


class MaximumRetryRequestsError(CrawlerError):
    def __init__(self):
        self.message = (
            "Request - Maximum number of retry attempts to execute request "
            "has been exceeded."
        )
        super().__init__(self.message)


class MaximumMissedAdError(CrawlerError):
    def __init__(self):
        self.message = (
            "Crawler - Maximum number of skipped Ads has been exceeded. "
            "Check correctness of Ad URL formation"
        )
        super().__init__(self.message)
