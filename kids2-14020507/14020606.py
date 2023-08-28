
# Required Parameter
# Optional Parameter

# def validate_national_code(
#         national_code: str,
#         gender: str = '',
#         flag: bool | None = None) -> bool:
#     """
#     این یک تابع برای بررسی کردن کد ملی می باشد.
#     :param gender:
#     :param flag:
#     :param national_code:  کد ملی
#     :return:
#     """
#     return True


# print(validate_national_code('1234569842'))  # positional Arg
# print(validate_national_code(national_code='1234569842'))  # keyword Arg
# print(validate_national_code('1234569842', flag=True))
# print(validate_national_code('1234569842', flag=True, gender='Male'))


# def thousand_separator(number):
#     number = int(number)
#     return '{0:,}'.format(number)

# print(thousand_separator(46543216546542))


# def arabic_to_eng_number(number):
#     number = str(number)
#     return number.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩', '01234567890123456789'))


# def phone_number_is_valid(phone_number):
#     phone_number = arabic_to_eng_number(phone_number)
#     if phone_number[0:2] == '09' and phone_number.isnumeric() and len(phone_number) == 11:
#         return True
#     else:
#         return False

# print(phone_number_is_valid('۳۵۱۲۴۳۲۱۵۶۳'))


# def validate_national_id(national_code):
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
# print(validate_national_id('1234567899'))
# الگوریتم کدملی


# def my_func(text, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(text)
#
#
# my_func('salam', 4, 5, 2, 3, 4, 5, user='anisa', flag=False)

# def jaam(a, b):
#     return a + b

# ##########################
import random
# import pandas as pd

# import calculator
import calculator as cl
from calculator import jaam, tafrigh

# vue.js - React - Angular -
# component

a = jaam(9, 10)
print(cl.name)
print(a)




