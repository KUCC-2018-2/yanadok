from django.db import connection


def selectTest():
    cursor = connection.cursor()
    query_string = "select * from user"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'id': row[0], 'nickname': row[1],
               'name': row[2], 'password': row[3],
               'email': row[4], 'university': row[5],
               'isCertified': row[6], 'dueDate': row[7]}
        posts.append(dic)

    return posts