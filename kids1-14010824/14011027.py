# function
# تابع

# a = 5 + 9

# print('hello')

# define
# def my_function(a, b):
#     c = (2*a) + (4*b)
#     return c
#
# f = my_function(5, 7)
# print(f)
#
# g = my_function(6, 2)
# print(g)
#
# w = my_function(1, 8)
# print(w)
#
# v = my_function(2, 9)
# print(v)
#
# j = my_function(2, 2)
# print(j)

# def check_input(a):
#     if a == 'salam':
#         return True
#     else:
#         return False

# d = check_input('byebye')
# print(d)
# print(check_input('byebye'))
# print(check_input('salam'))

# > <  ==  !=

# def check_national_code(national_code):
#     if len(national_code) != 10 or not national_code.isnumeric():
#         return False
#     controller_digit = 0
#     for i in range(0, 9):
#         controller_digit += int(national_code[i]) * (10 - i)
#     check_digit = controller_digit % 11
#     if int(national_code[9]) == check_digit and check_digit < 2:
#         return True
#     elif check_digit >= 2 and int(national_code[9]) == (11 - check_digit):
#         return True
#     else:
#         return False
#
# print(check_national_code('salam'))
# print(check_national_code('1234salam'))
# print(check_national_code('123'))
# print(check_national_code('1234567894'))
# print(check_national_code('3490905253'))

# def my_func():
#     return 'salam chetori?'
#
# print(my_func())


# def my_func2():
#     print('salam chetori?')
#
# print(my_func2())


# def my_func3(a, b):
#     c = a + b
#     d = a * b
#     e = a / b
#     return c, d, e
#
# q, x, z = my_func3(2, 3)
# print(q)
# print(x)
# print(z)

# ################################## #

# def get_score(a, score):
#     if a == 1:
#         score += 3
#     elif a == 2:
#         score += 2
#     elif a == 3:
#         a += 1
#     return score
#
# score = 0
# a = 10
# user_try = 1
# if a == 10:
#     print('afarin doros javab dadi!')
#     score = get_score(user_try, score)
# else:
#     print('eshtebah gofti')
#     user_try += 1

import random
my_list = ['sang', 'kaghaz', 'gheychi']
ai_choice = random.choice(my_list)
print(ai_choice)

a = input('sang kaghaz gheychi: ')
print(a)

# sang kaghaz gheychi
# 3 dast bazi anjam she
# user + 1
# ai + 1
# print

# a = input('sang kaghaz gheychi: ')




