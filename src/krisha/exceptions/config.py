from krisha.exceptions.base import CrawlerError


class CreateLogsDirError(CrawlerError):
    def __init__(self, error):
        self.message = f"Impossible to create a directory 'logs/' {error}"
        super().__init__(self.message)
