class YanadokBaseException(BaseException):
    def __init__(self, message=''):
        self.message = message


class BadRequestException(YanadokBaseException):
    pass


class NotFoundException(YanadokBaseException):
    pass


class InvalidArgumentException(YanadokBaseException):
    pass
