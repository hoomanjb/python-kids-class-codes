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

# run_query(sqlite_connection, create_table_query)
a = 'a'
b = 'b'
c = 'c'
d = 'd'
insert_users_query = f'''
    INSERT INTO
        users 
        (first_name, last_name, age, national_code)
        VALUES
        ({a}, {b}, {c}, {d})
        ;
'''

run_query(sqlite_connection, insert_users_query)
