# import time
#
#
# def clock(func):
#     def clocked(*args):
#         t0 = time.perf_counter()
#         result = func(*args)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_str = ', '.join(repr(arg) for arg in args)
#         print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
#
#         return result
#     return clocked
#
#
# @clock
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print('*' * 40, 'Calling factorial(5)')
# print('5! =', factorial(5))
# print('*' * 40, 'Calling factorial(50)')
# print('50! =', factorial(50))
# print('*' * 40, 'Calling factorial(300)')
# print('300! =', factorial(300))


# recursive
# factorial

# 1! = 1 * 1 = 1
# 2! = 1! * 2 = (1 * 1) * 2 = 2
# 3! = 2! * 3 = ((1 * 1) * 2) * 3 = 6
# 4! = 3! * 4 = (((1 * 1) * 2) * 3) * 4 = 24 = (1 * 2! * 3!)
# 5! = 4! * 5 .........


# def my_factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number * my_factorial(number - 1)
#
# print(my_factorial(300))

# ############################################################
# DataBase
# SQL = Structured Query Language , NOSQL
# storonha = fname,lname,phone,
# SQL = postgresql , mysql, mssql, maridb, .....
# NOSQL = MongoDB, redis, couchdb ....
# cache

# sqlite
import sqlite3

def lite_create_connection(name):
    connection = None
    try:
        connection = sqlite3.connect(name)
        print('Connection to Sqlite Ok.')
    except Exception as ex:
        print(ex)
    return connection

#mysql-connector-python
# import mysql
#
# connection = mysql.connector.connect(
#     host='localhost', user='admin', passwd='admin', database='felan'
# )

import psycopg2


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


cont1 = lite_create_connection('mydata.sqlite')
cont2 = postgres_create_connection(
    database='test', user='postgres', password='1234qwer',
    host='localhost', port=5432
)

# table , user , post , comment , like
# insert , get (select), update , delete
# data relation
