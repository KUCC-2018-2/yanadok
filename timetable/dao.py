# from django.db import connection
from .models import Course, Timetable
from django.apps import apps


user = apps.get_model('user', 'User')
post = apps.get_model('board', 'Post')


def select_user_timetable(user_id):
    temp_rows = Timetable.objects.filter(user_id=user_id)
    courselist = []
    for tr in temp_rows:
        row = Course.objects.filter(course_id=tr.course_id.course_id)
        dic = {'course_id': row[0].course_id, 'course_no': row[0].course_no,
               'semester': row[0].semester, 'university': row[0].university,
               'campus': row[0].campus, 'classification': row[0].classification,
               'course_name': row[0].course_name, 'professor': row[0].professor,
               'credit': row[0].credit, 'date_classroom': row[0].date_classroom,
               }
        courselist.append(dic)

    return courselist


def select_all_courses():
    rows = Course.objects.all()
    courselist = []
    for row in rows:
        dic = {'course_id': row.course_id, 'course_no': row.course_no,
               'semester': row.semester, 'university': row.university,
               'campus': row.campus, 'classification': row.classification,
               'course_name': row.course_name, 'professor': row.professor,
               'credit': row.credit, 'date_classroom': row.date_classroom,
               }
        courselist.append(dic)

    return courselist


def select_search_results_with_st(st, key_word):
    if st == 'course_no':
        rows = Course.objects.filter(course_no=key_word)
    elif st == 'course_name':
        rows = Course.objects.filter(course_name=key_word)
    else:
        rows = Course.objects.filter(professor=key_word)

    courselist = []
    for row in rows:
        dic = {'course_id': row.course_id, 'course_no': row.course_no,
               'semester': row.semester, 'university': row.university,
               'campus': row.campus, 'classification': row.classification,
               'course_name': row.course_name, 'professor': row.professor,
               'credit': row.credit, 'date_classroom': row.date_classroom,
               }
        courselist.append(dic)

    return courselist


def select_search_results(key_word):
    rows = Course.objects.filter(course_no=key_word) | Course.objects.filter(course_name=key_word) | Course.objects.filter(professor=key_word)
    courselist = []
    for row in rows:
        dic = {'course_id': row.course_id, 'course_no': row.course_no,
               'semester': row.semester, 'university': row.university,
               'campus': row.campus, 'classification': row.classification,
               'course_name': row.course_name, 'professor': row.professor,
               'credit': row.credit, 'date_classroom': row.date_classroom,
               }
        courselist.append(dic)

    return courselist


def update_timetable(selected_courselist, user_id):
    rows = Timetable.objects.filter(user_id=user_id)
    row_idlist = []
    for row in rows:
        row_idlist.append(row.course_id.course_id)

    selected_course_idlist = []
    for sc in selected_courselist:
        selected_course_idlist.append(sc['course_id'])

    for scid in selected_course_idlist:
        if scid not in row_idlist:
            Timetable.objects.create(user_id=user(id=user_id), course_id=Course(course_id=scid))

    for row_id in row_idlist:
        if row_id not in selected_course_idlist:
            Timetable.objects.filter(user_id=user_id, course_id=row_id).delete()


def select_all_posts(course_id):
    rows = post.objects.filter(course_id=course_id).order_by('-post_id')
    posts = []
    for row in rows:
        dic = {'post_id': row.post_id, 'user_id': row.user_id,
               'course_id': row.course_id, 'title': row.title,
               'password': row.password, 'content': row.content,
               'post_type': row.post_type, 'is_closed': row.is_closed,
               'upload_time': row.upload_time}
        posts.append(dic)

    return posts
