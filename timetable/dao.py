# from django.db import connection

from django.apps import apps

from course.models import Course
from .models import Timetable

user = apps.get_model('user', 'User')
post = apps.get_model('board', 'Post')


def select_user_timetable(user_id):
    temp_rows = Timetable.objects.filter(user_id=user_id)
    courselist = []
    for tr in temp_rows:
        row = Course.objects.get(course_id=tr.course.course_id).to_dict()
        row['id'] = tr.id
        courselist.append(row)

    return courselist


def select_all_courses():
    rows = Course.objects.all()
    courselist = []
    for row in rows:
        courselist.append(row.to_dict())

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
        courselist.append(row.to_dict())

    return courselist


def select_search_results(key_word):
    rows = Course.objects.filter(course_no=key_word) | Course.objects.filter(
        course_name=key_word) | Course.objects.filter(professor=key_word)
    courselist = []
    for row in rows:
        courselist.append(row.to_dict())

    return courselist



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
