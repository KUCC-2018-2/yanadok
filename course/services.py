from course.models import Course


def get_courses(user, criteria=None, search_keyword=""):
    queryset = Course.objects.filter(university=user.university)
    if criteria == 'course_no':
        return serialize(queryset.filter(course_no__contains=search_keyword).all())
    if criteria == 'course_name':
        return serialize(queryset.filter(course_name__contains=search_keyword).all())
    if criteria == "professor":
        return serialize(queryset.filter(professor__contains=search_keyword).all())

    return []


def serialize(course_list):
    return [course.to_dict() for course in course_list]
