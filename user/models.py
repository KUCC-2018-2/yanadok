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


class Course(models.Model):
    courseid = models.CharField(primary_key=True, max_length=20)
    classification = models.CharField(max_length=20, blank=True, null=True)
    course_name = models.CharField(max_length=20, blank=True, null=True)
    professor = models.CharField(max_length=20, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    classroom = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('user.User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid', blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    post_type = models.CharField(max_length=10, blank=True, null=True)
    id_closed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostLike(models.Model):
    userid = models.ForeignKey('user.User', models.DO_NOTHING, db_column='userid', primary_key=True)
    postid = models.ForeignKey(Post, models.DO_NOTHING, db_column='postid')

    class Meta:
        managed = False
        db_table = 'post_like'
        unique_together = (('userid', 'postid'),)


class TimeTable(models.Model):
    userid = models.ForeignKey('user.user', models.DO_NOTHING, db_column='userid', primary_key=True)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')

    class Meta:
        managed = False
        db_table = 'time_table'
        unique_together = (('userid', 'courseid'),)