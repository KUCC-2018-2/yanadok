from django.db import transaction

from course.models import Course
from timetable.exceptions import DuplicateTimetableException
from timetable.models import Timetable


def get_user_timetable(user):
    timetable_models = Timetable.objects.filter(user=user).all()\
        .prefetch_related('course')
    return [timetable_model.course.to_dict() for timetable_model in timetable_models]


@transaction.atomic
def add_course_to_timetable(user, course_id):
    course = Course.objects.get(pk=course_id)
    timetable_of_user = Timetable.objects.filter(user=user).all()
    for timetable in timetable_of_user:
        if timetable.is_overlapped(course):
            raise DuplicateTimetableException
    Timetable.objects.create(user=user, course=course)


def delete_course_from_timetable(user, course_id):
    Timetable.objects.filter(user=user, course_id=course_id).delete()
