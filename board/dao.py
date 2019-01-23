from django.db import connection


def getCourseList(user_id):
    cursor = connection.cursor()
    query_string = "select course.course_id, course_name from course, user, timetable where course.course_id = timetable.course_id and user.id = timetable.user_id and id=" + str(user_id)
    cursor.execute(query_string)
    rows = cursor.fetchall()
    courselist = []
    for row in rows:
        dic = {'course_id': row[0], 'course_name': row[1],}
        courselist.append(dic)

    return courselist


def getCourseName(course_id):
    cursor = connection.cursor()
    query_string = "select course_name from course where course_id=" + str(course_id)
    cursor.execute(query_string)
    rows = cursor.fetchall()

    return rows[0][0]


def getUserList(posts):
    userlist = []
    for post in posts:
        cursor = connection.cursor()
        query_string = "select username from user, post where post.user_id = user.id and post_id=" + str(post['post_id'])
        cursor.execute(query_string)
        rows = cursor.fetchall()
        userlist.append(rows[0][0])

    return userlist


def selectAllPosts(course_id):
    cursor = connection.cursor()
    query_string = "select * from post where course_id=" + str(course_id)
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'post_id': row[0], 'user_id': row[1],
               'course_id': row[2], 'title': row[3],
               'password': row[4], 'content': row[5],
               'post_type': row[6], 'is_closed': row[7],
               'date': row[8]}
        posts.append(dic)

    return posts

def selectStudyPosts(course_id):
    cursor = connection.cursor()
    query_string = "select * from post where post_type= '스터디/팀플' and course_id=" + str(course_id)
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'post_id': row[0], 'user_id': row[1],
               'course_id': row[2], 'title': row[3],
               'password': row[4], 'content': row[5],
               'post_type': row[6], 'is_closed': row[7],
               'date': row[8]}
        posts.append(dic)

    return posts



