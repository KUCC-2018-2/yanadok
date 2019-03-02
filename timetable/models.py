from django.db import models


class Timetable(models.Model):
    user = models.ForeignKey('user.User', models.DO_NOTHING, db_column='user_id')
    course = models.ForeignKey('course.Course', models.DO_NOTHING, db_column='course_id')

    def is_overlapped(self, course):
        return self.course.is_overlapped(course)

    class Meta:
        db_table = 'timetable'
        unique_together = (('user', 'course'),)
