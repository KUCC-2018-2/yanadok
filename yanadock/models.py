# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Likey(models.Model):
    userid = models.ForeignKey('user.User', models.DO_NOTHING, db_column='userid', primary_key=True)
    postid = models.ForeignKey('Post', models.DO_NOTHING, db_column='postid')

    class Meta:
        managed = False
        db_table = 'likey'
        unique_together = (('userid', 'postid'),)


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


class TimeTable(models.Model):
    userid = models.ForeignKey('user.user', models.DO_NOTHING, db_column='userid', primary_key=True)
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')

    class Meta:
        managed = False
        db_table = 'time_table'
        unique_together = (('userid', 'courseid'),)


