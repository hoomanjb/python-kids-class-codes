import sqlite3  # SQLITE

import psycopg2  # POSTGRES


def create_connection(path='test.db'):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('connection is ok!')
    except Exception as akbar:
        print(akbar)
    return connection

sqlite_connection = create_connection()

def run_query(connection, query_text):
    cursor = connection.cursor()
    try:
        cursor.execute(query_text)
        connection.commit()
        print('ok')
    except Exception as ex:
        print(ex)


create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    mobile INTEGER,
    national_code TEXT UNIQUE NOT NULL
);
'''

create_table_post = """
    CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""

create_table_like = """
    CREATE TABLE IF NOT EXISTS likes (
    id SERIAL PRIMARY KEY,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (id)
    FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""

create_table_comment = """
    CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (id)
    FOREIGN KEY (user_id) REFERENCES users (id)
    );
"""

# run_query(sqlite_connection, create_table_post)
# run_query(sqlite_connection, create_table_like)
# run_query(sqlite_connection, create_table_comment)


insert_users = """
    INSERT INTO users
    (id, first_name, last_name, age, national_code)
    VALUES
    (1, 'hooman', 'javan', 20, 123),
    (2, 'barbod', 'samiee', 25, 456),
    (3, 'pooya', 'raiesi', 30, 789),
    (4, 'fateme', 'hoseinpoor', 10, 741)
    ;
"""

# run_query(sqlite_connection, insert_users)

# insert_users = """
#     INSERT INTO users
#     (id, first_name, last_name, age, national_code)
#     VALUES
#     (5, 'hooman', 'javan', 20, 852)
#     ;
# """
#
# run_query(sqlite_connection, insert_users)

# insert_posts = """
#     INSERT INTO posts
#     (id, title, user_id)
#     VALUES
#     (1, 'post1', 1),
#     (2, 'post2', 1),
#     (3, 'post3', 2),
#     (4, 'post4', 3)
#     ;
# """
#
# run_query(sqlite_connection, insert_posts)

# a = 6
# b = 3
# c = 4
#
# insert_like = f"""
#     INSERT INTO likes
#     (id, post_id, user_id)
#     VALUES
#     ({a}, {b}, {c})
#     ;
# """

# run_query(sqlite_connection, insert_like)


def get_data(connection, query_text):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query_text)
        result = cursor.fetchall()
    except Exception as ex:
        print(ex)
    return result

# get_all_users = """
#     SELECT * FROM users;
# """
#
# a = get_data(sqlite_connection, get_all_users)
# for item in a:
#     print(item)


# get_all_users = """
#     SELECT first_name, age FROM users where age > 20;
# """
#
# a = get_data(sqlite_connection, get_all_users)
# for item in a:
#     print(item)


# get_all1 = """
#     SELECT ll.id, ll.post_id, u.first_name FROM likes ll
#     join users u on u.id = ll.user_id
#     where u.age > 20;
# """
#
# a = get_data(sqlite_connection, get_all1)
# for item in a:
#     print(item)


# get_all2 = """
#     SELECT u.age, u.id, p.id, p.title FROM users u
#     join posts p on p.user_id = u.id
#     where u.age >= 20 or u.age <= 30
# ;
# """
#
# a = get_data(sqlite_connection, get_all2)
# for item in a:
#     print(item)


# get_all3 = """
#     SELECT p.*, u.first_name FROM posts p
#     join users u on u.id = p.user_id
# """
#
# a = get_data(sqlite_connection, get_all3)
# for item in a:
#     print(item)

update_query = """
    UPDATE users
    set age = 50
    where id = 1
"""

run_query(sqlite_connection, update_query)
