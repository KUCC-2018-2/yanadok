from django.db import connection
from .models import Post

def get_courselist(user_id):
    cursor = connection.cursor()
    query_string = "select course.course_id, course_name from course, user, timetable where course.course_id = timetable.course_id and user.id = timetable.user_id and id=" + str(user_id)
    cursor.execute(query_string)
    rows = cursor.fetchall()
    courselist = []
    for row in rows:
        dic = {'course_id': row[0], 'course_name': row[1],}
        courselist.append(dic)

    return courselist


def get_course_name(course_id):
    cursor = connection.cursor()
    query_string = "select course_name from course where course_id=" + str(course_id)
    cursor.execute(query_string)
    rows = cursor.fetchall()

    return rows[0][0]


def get_userlist(posts):
    userlist = []
    for post in posts:
        cursor = connection.cursor()
        query_string = "select username from user, post where post.user_id = user.id and post_id=" + str(post['post_id'])
        cursor.execute(query_string)
        rows = cursor.fetchall()
        userlist.append(rows[0][0])

    return userlist


def select_all_posts(course_id):
    # cursor = connection.cursor()
    # query_string = "select * from post where course_id=" + str(course_id)
    # cursor.execute(query_string)
    # rows = cursor.fetchall()
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
    # cursor = connection.cursor()
    # query_string = "select * from post where course_id=" + str(course_id)
    # cursor.execute(query_string)
    # rows = cursor.fetchall()
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



