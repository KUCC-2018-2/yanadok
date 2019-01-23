from django.db import connection


def selectUserTimetable(userId):
    cursor = connection.cursor()
    query_string = "select course.course_id, course_no, semester, university, campus, classification, course_name, professor, credit, date_classroom from timetable, course where user_id=" + str(userId) + " AND course.course_id=timetable.course_id"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'course_id': row[0], 'course_no': row[1],
               'semester': row[2], 'university': row[3],
               'campus': row[4], 'classification': row[5],
               'course_name': row[6], 'professor': row[7],
               'credit': row[8], 'date_classroom': row[9]
               }
        posts.append(dic)

    return posts


def selectAllCourses():
    cursor = connection.cursor()
    query_string = "select * from course"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'course_id': row[0], 'course_no': row[1],
               'semester': row[2], 'university': row[3],
               'campus': row[4], 'classification': row[5],
               'course_name': row[6], 'professor': row[7],
               'credit': row[8], 'date_classroom': row[9]
               }
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
        dic = {'course_id': row[0], 'course_no': row[1],
               'semester': row[2], 'university': row[3],
               'campus': row[4], 'classification': row[5],
               'course_name': row[6], 'professor': row[7],
               'credit': row[8], 'date_classroom': row[9]
               }
        posts.append(dic)

    return posts


def selectSearchResults(key_word):
    cursor = connection.cursor()
    query_string = "select * from course where course_no =" + key_word + " or course_name = " + key_word + " or professor=" + key_word
    print(query_string)
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'course_id': row[0], 'course_no': row[1],
               'semester': row[2], 'university': row[3],
               'campus': row[4], 'classification': row[5],
               'course_name': row[6], 'professor': row[7],
               'credit': row[8], 'date_classroom': row[9]
               }
        posts.append(dic)

    return posts


def updateTimetable(splist, userId):
    cursor = connection.cursor()
    rows = selectUserTimetable(userId)

    for n in range(0, len(splist)):
        if splist[n] not in rows:
            query_string = "insert into timetable (user_id, course_id) values (" + str(userId) + ", " + str(splist[n]['course_id']) + ')'
            cursor.execute(query_string)

    for n in range(0, len(rows)):
        if rows[n] not in splist:
            query_string = "delete from timetable where course_id=" + str(rows[n]['course_id']) + " and user_id=" + str(userId)
            cursor.execute(query_string)
    print(rows)
