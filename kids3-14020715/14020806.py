import psycopg2
import sqlite3


def postgres_create_connection(database, user, password, host, port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=database, user=user, password=password,
            host=host, port=port
        )
        print('Connection to postgres Ok.')
    except Exception as ex:
        print(ex)
    return connection


def lite_create_connection(name):
    connection = None
    try:
        connection = sqlite3.connect(name)
        print('Connection to Sqlite Ok.')
    except Exception as ex:
        print(ex)
    return connection


lite_connection = lite_create_connection('mydata.sqlite')
post_connection = postgres_create_connection(
    database='test', user='postgres', password='1234qwer',
    host='localhost', port=5432
)

# post = content, created_date, user_id
# user = first_name, last_name, age, phone_number
# like = post_id, user_id
# comment = content, post_id, user_id

create_users_table_sqlite = """
CREATE TABLE IF NOT EXISTS users (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age TEXT ,
    phone_number TEXT 
);
"""


create_post_table_sqlite = """
CREATE TABLE IF NOT EXISTS post (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at DATE NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_like_table_sqlite = """
CREATE TABLE IF NOT EXISTS likes (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_comment_table_sqlite = """
CREATE TABLE IF NOT EXISTS comment (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_users_table_postgres = """
CREATE TABLE IF NOT EXISTS users (
    id  SERIAL PRIMARY KEY ,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age TEXT ,
    phone_number TEXT 
);
"""


create_post_table_postgres = """
CREATE TABLE IF NOT EXISTS post (
    id  SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at DATE NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users (id)
);
"""

create_like_table_postgres = """
CREATE TABLE IF NOT EXISTS likes (
    id  SERIAL PRIMARY KEY ,
    post_id INTEGER NOT NULL REFERENCES post (id),
    user_id INTEGER NOT NULL REFERENCES users (id)
);
"""

create_comment_table_postgres = """
CREATE TABLE IF NOT EXISTS comment (
    id  SERIAL PRIMARY KEY ,
    content TEXT NOT NULL,
    post_id INTEGER NOT NULL REFERENCES post (id),
    user_id INTEGER NOT NULL REFERENCES users (id)
);
"""

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('query  ok')
    except Exception as ex:
        print(ex)


# execute_query(lite_connection, create_users_table_sqlite)
# execute_query(lite_connection, create_post_table_sqlite)
# execute_query(lite_connection, create_comment_table_sqlite)
# execute_query(lite_connection, create_like_table_sqlite)

# execute_query(post_connection, create_users_table_postgres)
# execute_query(post_connection, create_post_table_postgres)
# execute_query(post_connection, create_comment_table_postgres)
# execute_query(post_connection, create_like_table_postgres)

# insert_users = """
# INSERT INTO users (first_name, last_name, age, phone_number)
#  VALUES
#   ('Ali', 'rezaii', 25, '+989121234567'),
#   ('Anisa', 'test', 15, null),
#   ('Reza', 'pishro', 45, null);
# """
# execute_query(lite_connection, insert_users)

# users = [
#     ('Ali', 'rezaii', 25, '+989121234567'),
#     ('Anisa', 'test', 15, None),
#     ('Reza', 'pishro', 45, None)
# ]
#
# user_record = ', '.join(['%s'] * len(users))
#
# insert_query = (
#     f'INSERT INTO users (first_name, last_name, age, phone_number) Values {user_record}'
# )
# post_connection.autocommit = True
# cursor = post_connection.cursor()
# cursor.execute(insert_query, users)

select_all_users = """
SELECT first_name from users
"""
cursor = post_connection.cursor()
cursor.execute(select_all_users)
users = cursor.fetchall()
print(users)