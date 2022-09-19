# 5ta soal beporsim
# agar doros javab dad +1
# agar eshtebah javab dad -1
# 3bar ham talash kone

# q1 = 'natijeye amaliate 2 + 2 che mishavad? a-5  b-4  : '
# q2 = 'bozorg tarin heyvane khoshki? 1-fil 2-asb'
# q3 = 'por sorat tarin internet bara che keshvari ast? 1-iran  2-japon'
# q4 = 'natijeye 10 * 2 che mishavad? a-10  b-20'
# q5 = 'bishtarin tamadon bara che keshvari ast? 1-china  2-iran'
#
# plus_score = 0
# negative_score = 0
#
# for item in range(3):
#     user_input = input(q1)
#     if user_input == '4' or user_input == 'b':
#         print('Correct')
#         plus_score += 1
#         break
#     else:
#         if item == 2:
#             print('Dg nemitooni talash koni')
#             negative_score += 1
#         else:
#             print('Eshtebah javab dadi hanooz mitooni talash koni')
#
# for item in range(3):
#     user_input = input(q2)
#     if user_input == '1' or user_input == 'fill':
#         print('Correct')
#         plus_score += 1
#         break
#     else:
#         if item == 2:
#             print('Dg nemitooni talash koni')
#             negative_score += 1
#         else:
#             print('Eshtebah javab dadi hanooz mitooni talash koni')
#
# for item in range(3):
#     user_input = input(q3)
#     if user_input == '1' or user_input == 'iran':
#         print('Correct')
#         plus_score += 1
#         break
#     else:
#         if item == 2:
#             print('Dg nemitooni talash koni')
#             negative_score += 1
#         else:
#             print('Eshtebah javab dadi hanooz mitooni talash koni')
#
# for item in range(3):
#     user_input = input(q4)
#     if user_input == 'b' or user_input == '20':
#         print('Correct')
#         plus_score += 1
#         break
#     else:
#         if item == 2:
#             print('Dg nemitooni talash koni')
#             negative_score += 1
#         else:
#             print('Eshtebah javab dadi hanooz mitooni talash koni')
#
# for item in range(3):
#     user_input = input(q5)
#     if user_input == '2' or user_input == 'iran':
#         print('Correct')
#         plus_score += 1
#         break
#     else:
#         if item == 2:
#             print('Dg nemitooni talash koni')
#             negative_score += 1
#         else:
#             print('Eshtebah javab dadi hanooz mitooni talash koni')
#
# print('bazi tamam shod')
# print(f'shoma {plus_score} soal ro dorost javab dadid.')
# print(f'shoma {negative_score} soal ro eshtebah javab dadid.')

# ####################################################################
# DRY    (Dont Repeat Yourself)


# define
# def harchi_aaa(a, b):
#     c = (a + b) * 2
#     return c
#
# x = harchi_aaa(10, 5)
# print(x)

# def my_function(a):
#     b = a + 10
#     c = b + 3
#     print(c)
#
# my_function(14)
# my_function(4)
# my_function(5)
# my_function(6)
# my_function(7)
# my_function(2)
# my_function(5)
# my_function(6)
# my_function(11)
# my_function(12)
# my_function(45)
# my_function(54)


# q1 = 'natijeye amaliate 2 + 2 che mishavad? a-5  b-4  : '
# q2 = 'bozorg tarin heyvane khoshki? 1-fil 2-asb'
# q3 = 'por sorat tarin internet bara che keshvari ast? 1-iran  2-japon'
# q4 = 'natijeye 10 * 2 che mishavad? a-10  b-20'
# q5 = 'bishtarin tamadon bara che keshvari ast? 1-china  2-iran'
#
# plus_score = 0
# negative_score = 0
#
# def validate(soal, javab):
#     for item in range(3):
#         user_input = input(soal)
#         if user_input in javab:
#             print('Correct')
#             return True
#         else:
#             if item == 2:
#                 print('Dg nemitooni talash koni')
#                 return False
#             else:
#                 print('Eshtebah javab dadi hanooz mitooni talash koni')
#
#
# result1 = validate(q1, ['b', '4'])
# result2 = validate(q2, ['1', 'fill'])
# result3 = validate(q3, ['1', 'iran'])
# result4 = validate(q4, ['b', '20'])
# result5 = validate(q5, ['iran', '2'])
#
# if result1:
#     plus_score += 1
# else:
#     negative_score += 1
# if result2:
#     plus_score += 1
# else:
#     negative_score += 1
# if result3:
#     plus_score += 1
# else:
#     negative_score += 1
# if result4:
#     plus_score += 1
# else:
#     negative_score += 1
# if result5:
#     plus_score += 1
# else:
#     negative_score += 1
#
# print('bazi tamam shod')
# print(f'shoma {plus_score} soal ro dorost javab dadid.')
# print(f'shoma {negative_score} soal ro eshtebah javab dadid.')

# def jaam(a, b):
#     result = a + b
#     return result
#
# def tafrigh(a, b):
#     result = a - b
#     return result
#
# def taghsim(a, b):
#     result = a / b
#     return result
#
# def zarb(a, b):
#     result = a * b
#     return result
#
# s = jaam(5, 3)
# print(s)
# v = tafrigh(84, 2)
# print(v)
# b = taghsim(47, 7)
# print(b)
# m = zarb(7, 3)
# print(m)



# import turtle
# import random
#
# def entekhabe_tasadofi(a):
#     result = random.choice(a)
#     return result
#
# b = entekhabe_tasadofi([1, 5, 7, 3, 2, 7, 9, 10, 33, 34, 56, 32, 67])
# print(b)

# tamrin
# sang kaghaz gheychi  5 dast
# player shoma player ai
# kaghaz - sang   +1 user  0 ai
# kaghaz

