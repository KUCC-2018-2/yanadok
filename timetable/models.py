from django.db import models


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_no = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    university = models.CharField(max_length=20)
    campus = models.CharField(max_length=20)
    classification = models.CharField(max_length=20)
    course_name = models.CharField(max_length=20)
    professor = models.CharField(max_length=20, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    date_classroom = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'course'
        unique_together = (('course_id', 'course_no', 'semester', 'university', 'campus'),)


class Timetable(models.Model):
    user = models.ForeignKey('user.User', models.DO_NOTHING, primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'timetable'
        unique_together = (('user', 'course'),)
