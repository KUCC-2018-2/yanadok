class YanadokBaseException(BaseException):
    status = 500

    def __init__(self, message=''):
        self.message = message


class BadRequestException(YanadokBaseException):
    status = 400


class NotFoundException(YanadokBaseException):
    status = 404


class InvalidArgumentException(BadRequestException):
    pass
