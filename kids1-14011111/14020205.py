# print(2+9)


# def my_func():
#     print(1)
#     print(2)
#     print(3)
#     return 5
#
# a = my_func()
# print(a)

# def func1():
#     return 'salam1'
#
# def func2():
#     return 'salam2'
#
# def func3():
#     print(func1())
#     print(func2())
#     return 'salam3'
#
# print(func3())


# def checking_number(user_input):
#     for item in user_input:  # '123salam'
#         if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             print('voroodi eshtebah dobare talash konid!')
#             return True
#     return False
#
#
# name = input('enter your name: ')
#
# while True:
#     is_true = True
#     while is_true:
#         a1 = input('addad avalo begoo: ') #a1 = salam
#         is_true = checking_number(a1)
#
#     is_true = True
#     while is_true:
#         a2 = input('addad dovom begoo: ')
#         is_true = checking_number(a2)
#
#     operator = input('kodomo mikhay? + - * / exit restart')
#     if operator == '+':
#         print(int(a1) + int(a2))
#     elif operator == '-':
#         print(int(a1) - int(a2))
#     elif operator == '*':
#         print(int(a1) * int(a2))
#     elif operator == '/':
#         print(int(a1) / int(a2))
#     elif operator == 'exit':
#         print('BYE,BYE')
#         break
#     elif operator == 'restart':
#         continue
#     else:
#         print('amalgare eshtebah!')

import random

def make_password():
    counter = int(input('chanta charecter bashe? '))  # 10
    is_lower = input('horoofe koochik bashe? ')  # ok
    is_upper = input('horoofe bozorg bashe? ')  # ok
    is_number = input('horoofe addadi bashe? ')  # no

    maker = ''
    if is_lower == 'ok':
        maker += 'qwertyuiopasdfghjklzxcvbnm'
    if is_upper == 'ok':
        maker += 'QWERTYUIOPASDFGHJKLZXCVBNM'
    if is_number == 'ok':
        maker += '1234567890'

    # maker = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    password = ''
    for item in range(counter):
        password += random.choice(maker)

    return password


print(make_password())
