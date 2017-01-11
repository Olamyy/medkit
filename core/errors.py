class JabbError(Exception):
    def __init__(self, message=None, http_status=None):
        super(JabbError, self).__init__(message)

        self.message = message
        self.http_status = http_status


class InvalidFreezeFileError(JabbError):
    """
    Invalid FreezeFile
    """
    pass


class InvalidQueryError(JabbError):
    """
    Invalid DB Query
    """
    pass


class InvalidFileExtension(JabbError):
    """

    """
    pass


class InvalidUrlError(JabbError):
    """

    """
    pass
