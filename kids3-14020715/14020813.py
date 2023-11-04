import psycopg2
import sqlite3


def postgres_create_connection(database, user, password, host, port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=database, user=user, password=password,
            host=host, port=port
        )
    except Exception as ex:
        print(ex)
    return connection


def lite_create_connection(name):
    connection = None
    try:
        connection = sqlite3.connect(name)
    except Exception as ex:
        print(ex)
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Exception as ex:
        print(ex)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"The error '{e}' occurred")

def execute_read_query_just_one_result(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"The error '{e}' occurred")

lite_connection = lite_create_connection('mydata.sqlite')
post_connection = postgres_create_connection(
    database='test', user='postgres', password='1234qwer',
    host='localhost', port=5432
)



# select_all_users = """
# SELECT * from users
# """
#
# users = execute_read_query(lite_connection, select_all_users)
# for item in users:
#     print(item)

# select_all_posts = """
# SELECT * from post
# """
#
# posts = execute_read_query(lite_connection, select_all_posts)
# for item in posts:
#     print(item)


# insert_users = """
# INSERT INTO post (content, created_at, user_id)
#  VALUES
#   ('content 4', '2022-11-05', 5 )
# ;
# """
# execute_query(post_connection, insert_users)

# select_all_users = """
# SELECT * from users
# """
#
# users = execute_read_query(post_connection, select_all_users)
# for item in users:
#     print(item)
#
# print('#' * 50)
# select_all_posts = """
# SELECT * from post
# """
#
# posts = execute_read_query(post_connection, select_all_posts)
# for item in posts:
#     print(item)
# print('#' * 50)
#
# select_all_comment = """
# SELECT * from comment
# """
#
# comment = execute_read_query(post_connection, select_all_comment)
# for item in comment:
#     print(item)
# print('#' * 50)
#
# select_all_posts = """
# SELECT ps.id, ps.content , ur.first_name, ur.last_name, cm.content from post ps
# Inner join users ur on ur.id = ps.user_id
# inner join comment cm on ps.id = cm.post_id
# """
# # Outer join , left join ...
#
# posts = execute_read_query(post_connection, select_all_posts)
# for item in posts:
#     print(item)

# query = """
# select * from post
# where user_id = 1;
# """
#
# posts = execute_read_query(post_connection, query)
# for item in posts:
#     print(item)

# user shomare 1 baraye post shomare 3 che commenti gozashte

# query = """
# select content from comment
# where user_id = 1 and post_id = 3 ;
# """
#
# posts = execute_read_query(post_connection, query)
# for item in posts:
#     print(item)




# result = execute_read_query_just_one_result(post_connection, query)
# result2 = execute_read_query(post_connection, query)
#
# print(result)
# print(result2)

# get_query = """
# select * from comment
# where user_id = 1 and post_id = 2 ;
# """
#
# update_query = """
# UPDATE
#     comment
# SET
#     content = 'salam chetori?'
# WHERE user_id = 1 and post_id = 2;
# """
# result = execute_read_query(post_connection, get_query)
# print(result)
# execute_query(post_connection, update_query)
# result = execute_read_query(post_connection, get_query)
# print(result)


delete_query = 'DELETE FROM users WHERE id = 3;'
execute_query(post_connection, delete_query)
