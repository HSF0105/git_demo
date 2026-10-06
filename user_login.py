import sqlite3 as sql

def check_user(user_name):
    connection = sql.connect("user.db")
    cursor = connection.cursor()
    cursor.execute("SELECT user_id from user")
    users = cursor.fetchall()
    if user_name in users:
        print('Exsisting user')
    else:
        print("No such user exist")
