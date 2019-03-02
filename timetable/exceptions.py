from yanadok.exceptions import BadRequestException


class DuplicateTimetableException(BadRequestException):
    def __init__(self):
        super().__init__('이미 시간표에 담은 강의입니다.')
