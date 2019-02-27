from django.db import transaction

from timetable.models import Timetable
from course.models import Course


@transaction.atomic
def add_course_to_timetable(user, course_id):
    course = Course.objects.get(pk=course_id)
    Timetable.objects.create(user=user, course=course)


