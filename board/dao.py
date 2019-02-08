# from django.db import connection
from .models import Post, PostLike, Comment
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


def select_notice_posts(course_id):
    rows = Post.objects.filter(course_id=course_id).order_by('-post_id')
    posts = []
    for row in rows:
        like_row = PostLike.objects.filter(post_id=row.post_id)
        if len(like_row) >= 10:
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


def get_search_results(course_id, key_word):
    rows = Post.objects.filter(course_id=course_id).filter(title__icontains=key_word).order_by('-post_id')
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
        PostLike.objects.create(post_id=Post(post_id=post_id), user_id=user(id=user_id))


def delete_like(post_id, user_id):
    PostLike.objects.filter(post_id=Post(post_id=post_id)).filter(user_id=user(id=user_id)).delete()


def insert_comment(post_id, user_id, comment_content):
    Comment.objects.create(post_id=Post(post_id=post_id), user_id=user(id=user_id), comment_content=comment_content)


def select_all_comments(post_id):
    rows = Comment.objects.filter(post_id=Post(post_id=post_id)).order_by('comment_id')
    comments = []
    for row in rows:
        dic = {'comment_id': row.comment_id, 'comment_content': row.comment_content,
               'post_id': row.post_id, 'user_id': row.user_id,
               'upload_time': row.upload_time, }
        comments.append(dic)

    return comments

def delete_comment(comment_id, user_id):
    rows = Comment.objects.filter(user_id=user(id=user_id)).order_by('comment_id')

    for row in rows:
        if row.comment_id == int(comment_id):
            Comment.objects.filter(comment_id=comment_id).delete()

