from django.db import models


class Timetable(models.Model):
    user = models.ForeignKey('user.User', models.DO_NOTHING, db_column='user_id', primary_key=True)
    course = models.ForeignKey('course.Course', models.DO_NOTHING, db_column='course_id')

    class Meta:
        managed = False
        db_table = 'timetable'
        unique_together = (('user', 'course'),)
