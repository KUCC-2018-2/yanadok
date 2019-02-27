from course.models import Course


def get_courses(user, criteria=None, search_keyword=""):
    if criteria == 'course_no':
        return Course.objects.filter(university=user.university, course_no__contains=search_keyword).all()
    if criteria == 'course_name':
        return Course.objects.filter(university=user.university, course_name__contains=search_keyword).all()
    if criteria == "professor":
        return Course.objects.filter(university=user.university, professor__contains=search_keyword).all()

    return Course.objects.filter(university=user.university).all()
