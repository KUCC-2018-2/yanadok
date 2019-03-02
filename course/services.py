from django.forms import model_to_dict

from course.models import Course


def get_courses(user, criteria=None, search_keyword=""):
    queryset = Course.objects.filter(university=user.university)
    if criteria == 'course_no':
        queryset = queryset.filter(course_no__contains=search_keyword)
    if criteria == 'course_name':
        queryset = queryset.filter(course_name__contains=search_keyword)
    if criteria == "professor":
        queryset = queryset.filter(professor__contains=search_keyword)

    return serialize(queryset.all())


def serialize(course_list):
    return [course.to_dict() for course in course_list]
