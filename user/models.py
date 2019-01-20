from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=10, blank=True, null=True)
    university = models.CharField(max_length=20, default="KoreaUniv")
    iscertified = models.IntegerField(db_column='is_certified', default=0)  # Field name made lowercase.
    duedate = models.DateField(db_column='due_date', null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'
