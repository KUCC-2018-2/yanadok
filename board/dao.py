# from django.db import connection
from .models import Post, PostLike
from django.apps import apps


course = apps.get_model('timetable', 'Course')
timetable = apps.get_model('timetable', 'Timetable')
user = apps.get_model('user', 'User')


def get_courselist(user_id):
    temp_rows = timetable.objects.filter(user_id=user_id)

    courselist = []
    for tr in temp_rows:
        row = course.objects.filter(course_id=tr.course_id.course_id)
        dic = {'course_id': row[0].course_id, 'course_name': row[0].course_name,}
        courselist.append(dic)

    return courselist


def get_course_name(course_id):
    rows = course.objects.filter(course_id=course_id)

    return rows[0].course_name


def get_userlist(posts):
    userlist = []
    for post in posts:
        userlist.append(post.get('user_id'))

    return userlist


def select_all_posts(course_id):
    rows = Post.objects.filter(course_id=course_id).order_by('-post_id')
    posts = []
    for row in rows:
        dic = {'post_id': row.post_id, 'user_id': row.user_id,
               'course_id': row.course_id, 'title': row.title,
               'password': row.password, 'content': row.content,
               'post_type': row.post_type, 'is_closed': row.is_closed,
               'upload_time': row.upload_time}
        posts.append(dic)

    return posts


def select_study_posts(course_id):
    rows = Post.objects.filter(course_id=course_id).filter(post_type='스터디/팀플').order_by('-post_id')
    posts = []
    for row in rows:
        dic = {'post_id': row.post_id, 'user_id': row.user_id,
               'course_id': row.course_id, 'title': row.title,
               'password': row.password, 'content': row.content,
               'post_type': row.post_type, 'is_closed': row.is_closed,
               'upload_time': row.upload_time}
        posts.append(dic)

    return posts


def select_post(post_id):
    row = Post.objects.filter(post_id=post_id)

    dic = {'post_id': row[0].post_id, 'user_id': row[0].user_id,
           'course_id': row[0].course_id, 'title': row[0].title,
           'password': row[0].password, 'content': row[0].content,
           'post_type': row[0].post_type, 'is_closed': row[0].is_closed,
           'upload_time': row[0].upload_time}

    return dic


def like_active(post_id, user_id):
    row = PostLike.objects.filter(post_id=post_id, user_id=user_id)

    return len(row) != 0


def get_like_num(post_id):
    row = PostLike.objects.filter(post_id=post_id)

    return len(row)


def insert_like(post_id, user_id):
    if PostLike is not None and user_id is not None:
        user = apps.get_model('user', 'User')
        PostLike.objects.create(post_id=Post(post_id=post_id), user_id=user(id=user_id))


def delete_like(post_id, user_id):
    user = apps.get_model('user', 'User')
    PostLike.objects.filter(post_id=Post(post_id=post_id)).filter(user_id=user(id=user_id)).delete()



