from django.db import connection


def selectUserTimetable(userId):
    cursor = connection.cursor()
    query_string = "select course.course_id, semester, school, campus, classification, course_name, professor, credit, date_classroom from timetable, course where user_id=" + str(userId) + " AND course.course_id=timetable.course_id"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'course_id': row[0], 'semester': row[1],
               'school': row[2], 'campus': row[3],
               'classification': row[4], 'course_name': row[5],
               'professor': row[6], 'credit': row[7],
               'date_classroom': row[8]}
        posts.append(dic)

    return posts


def selectAllCourses():
    cursor = connection.cursor()
    query_string = "select * from course"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'course_id': row[0], 'semester': row[1],
               'school': row[2], 'campus': row[3],
               'classification': row[4], 'course_name': row[5],
               'professor': row[6], 'credit': row[7],
               'date_classroom': row[8]}
        posts.append(dic)

    return posts


def selectSearchResultsWithST(st, key_word):
    cursor = connection.cursor()
    query_string = "select * from course where " + st + "=" + key_word
    print(query_string)
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'course_id': row[0], 'semester': row[1],
               'school': row[2], 'campus': row[3],
               'classification': row[4], 'course_name': row[5],
               'professor': row[6], 'credit': row[7],
               'date_classroom': row[8]}
        posts.append(dic)

    return posts


def selectSearchResults(key_word):
    cursor = connection.cursor()
    query_string = "select * from course where course_id =" + key_word + " or course_name = " + key_word + " or professor=" + key_word
    print(query_string)
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'course_id': row[0], 'semester': row[1],
               'school': row[2], 'campus': row[3],
               'classification': row[4], 'course_name': row[5],
               'professor': row[6], 'credit': row[7],
               'date_classroom': row[8]}
        posts.append(dic)

    return posts


def updateTimetable(splist, userId):
    cursor = connection.cursor()
    # query_string = "delete from timetable where user_id=2"
    # cursor.execute(query_string)
    rows = selectUserTimetable(userId)

    for n in range(0, len(splist)):
        if splist[n] not in rows:
            query_string = "insert into timetable (user_id, course_id) values (2, " + '"' + splist[n]['course_id'] + '")'
            cursor.execute(query_string)

    for n in range(0, len(rows)):
        if rows[n] not in splist:
            query_string = "delete from timetable where course_id=" + '"' + rows[n]['course_id'] + '"'
            cursor.execute(query_string)
    print(rows)
