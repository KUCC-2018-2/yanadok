from yanadok.exceptions import YanadokBaseException


class DuplicateUserException(YanadokBaseException):
    def __init__(self):
        super().__init__("이미 존재하는 이메일입니다.")
