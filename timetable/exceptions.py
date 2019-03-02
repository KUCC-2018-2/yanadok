from yanadok.exceptions import BadRequestException


class DuplicateTimetableException(BadRequestException):
    def __init__(self):
        super().__init__('시간표에 겹치는 강의가 존재합니다..')
