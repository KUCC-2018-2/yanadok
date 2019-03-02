import re

from django.contrib.auth.models import AbstractUser
from django.db import models

from yanadok.exceptions import InvalidArgumentException


class User(AbstractUser):
    UNIVERSITY_CHOICE = (
        ('고려대학교', '고려대학교'),
        ('연세대학교', '연세대학교'),
        ('서울대학교', '서울대학교'),
    )
    nickname = models.CharField(max_length=10, blank=True, null=True)
    university = models.CharField(max_length=20, default="고려대학교", choices=UNIVERSITY_CHOICE)
    duedate = models.DateField(db_column='due_date', null=True)  # Field name made lowercase.

    @staticmethod
    def from_registration_info(body):
        User.__validate_fields(body)
        user = User(email=body['email'],
                    username=body['email'],
                    university=body['university'],
                    first_name=body['name'],
                    nickname=body['nickname'])
        user.set_password(body['password'])
        # user.is_active = False
        return user

    @staticmethod
    def __validate_fields(body):
        for key in ['email', 'university', 'password', 'name', 'nickname']:
            if not body.get(key, False):
                raise InvalidArgumentException('입력되지 않은 필드가 있습니다.')

        if not re.match(r'[^@]+@[^@]+\.[^@]+', body['email']):
            raise InvalidArgumentException('잘못된 이메일 형식입니다.')

        if len(body['password']) < 8:
            raise InvalidArgumentException('비밀번호가 너무 짧습니다.')

        if len(body['nickname']) < 2:
            raise InvalidArgumentException('닉네임이 너무 짧습니다.')

    class Meta:
        db_table = 'user'
