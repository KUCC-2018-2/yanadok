from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    UNIVERSITY_CHOICE = (
        ('고려대학교', '고려대학교'),
        ('연세대학교', '연세대학교'),
        ('서울대학교', '서울대학교'),
    )
    nickname = models.CharField(max_length=10, blank=True, null=True)
    university = models.CharField(max_length=20, default="고려대학교", choices=UNIVERSITY_CHOICE)
    duedate = models.DateField(db_column='due_date', null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'

