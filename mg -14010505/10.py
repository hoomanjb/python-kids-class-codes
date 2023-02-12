# Integer (..., -1, 0, 1, ...)
# Float ()
# Boolean
# String
# List

# if , else , elif

# a = 5
# b = 7
# if a < b:
#     print('ok')

# and , or

# loop , (while , for)

# ##################
# function = تابع   -> functions = توابع


# define - a and b is arguments
# def my_function(a, b):
#     c = (a * b) + 10
#     return c
#
# 10 and 2 are positional parameters
# d = my_function(10, 2)
# print(d)
# e = my_function(9, 3)
# print(e)
# f = my_function(8, 12)
# print(f)
# g = my_function(22, 2)
# print(g)
# h = my_function('salam', 2)
# print(h)

#
# def print_hello():
#     a = 10
#     b = 20
#     return 'Hellooooooooooo'
#
# a = print_hello()
# print(a)

# ####################################### #
# guess Numbers
# (0 - 50)
# 34
# input() -> 20 -> guess upper
# come lower

# import random
#
# my_number = random.randint(0, 50)
# print(f'my number is: {my_number}')
# start, end = 0, 50
# while True:
#     try:
#         user_input = int(input(f'plz enter number btw ({start}-{end}): '))
#     except ValueError as value_error:
#         print(f'plz enter numbers! error is: {value_error}')
#     else:
#         if user_input == my_number:
#             print('That is Correct...!')
#             print('Game Over!')
#             break
#         elif user_input > my_number:   # 45 > 34
#             print('plz enter a lower number! ')
#             if user_input < end:
#                 end = user_input  # (0 - 50) - 35 -> 40 -> (0, 40)
#         else:
#             print('plz enter a higher number! ')
#             if user_input > start:
#                 start = user_input

# Error Handling

# a = input('enter number 1: ')
# b = input('enter number 2: ')
# try:
#     c = int(a) / int(b)
# except ValueError as value_error:
#     print(value_error)
# except ZeroDivisionError as div_error:
#     print(div_error)
# except Exception as error:
#     print(error)
# else:
#     print(c)
# finally:
#     print('At last')

#  #############################  #
