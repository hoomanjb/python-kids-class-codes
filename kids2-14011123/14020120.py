# import string
# import random
# print('SALAM Khosh AMADID')
#
# while True:
#     try:
#         pass_counter = int(input("PASS Counter: "))
#         break
#     except Exception as ex:
#         print('You Must choose From Int Numbers!')
#
#
# def check_answer(answer):
#     if answer == '1' or answer.lower() == 'yes' or answer.lower() == 'y':
#         return True
#     else:
#         return False
#
# has_number = input('has Number [0-9]? Yes=1=y or No=0=n :')  # yes, yEs, YeS, YES, YEs, yEs - Y, y
# has_upper_case = input('has upper_case [A-Z]? Yes=1=y or No=0=n :')
# has_lower_case = input('has lower_case [a-z]? Yes=1=y or No=0=n :')
# has_spec_char = input('has spec_char [!@#$%^&*()-_=/.]? Yes=1=y or No=0=n :')
#
# choices = ''
# choices += string.digits if check_answer(has_number) else ' '
# choices += string.ascii_uppercase if check_answer(has_upper_case) else ' '
# choices += string.ascii_lowercase if check_answer(has_lower_case) else ' '
# choices += string.punctuation if check_answer(has_spec_char) else ' '
#
# password = ''
# for item in range(pass_counter):
#     password += random.choice(choices)
#
# print(password)


# import random, string
#
# print("be password saz ma khosh amadid")
#
# while True:
#     try:
#         length = int(input("chand eagham bashe : "))
#     except Exception as error:
#         continue
#     has_lowercase = input("hooroof bozorg dashte bashe (y/n) ").lower()
#     has_uppercase = input("hooroof kuchik dashte bashe (y/n) ").lower()
#     has_digits = input("addad dashte bashe (y/n) ").lower()
#     has_special_chars = input("hooroof khas dashte bashe (y/n) ").lower()
#
#     options = []
#     if has_lowercase == "y":
#         options += list(string.ascii_lowercase)
#     if has_uppercase == "y":
#         options += list(string.ascii_uppercase)
#     if has_digits == "y":
#         options += list(string.digits)
#     if has_special_chars == "y":
#         options += list(string.punctuation)
#
#     password = ''
#     for i in range(length):
#         password += random.choice(options)
#
#     print("password shoma hast : ", password)

# ##############################################################
# Function

# Parameter: a, b  = ورودی یا پارامتر
# Required Par = اجباری
# Optional Par = اختیاری

# def test(a: int | float, b: int | float, d: str = 'Test') -> int | float:
#     '''
#     in function baraye test sakhte shode
#     :param a: vorodi aval ejbari va bayad az int ya float bashe
#     :param b: vorodi dovom ejbari va bayad az int ya float bashe
#     :param d: vorodi ekhtiari
#     :return: yek adade float ya int
#     '''
#     c = a + b
#     print(d)
#     return c


# Argument: 6 ,8  = ورودی های ما یا آرگیومنت
# Positional Arg
# Keyword Arg

# print(test(6, 8))  # Positional Arg
# print(test(b=9, a=7))  # Keyword Arg


# print(test(a='salam', b=5))

# print(test(a=6, b=8))
# print(test(b=9.2, a=5))
# print(test(d='salam', a=7, b=6))

# #######################################
# log ya email ya sms
# decorator - DB - Log - Metric - Signal
# DB - table - userha - sms


# def test(a, b, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     return a + b
#
# print(test(19, 23, 99, c=8, d=9))

# class A:
#
#     def __add__(self, other):
#         return other - 20
#
# b = A()
# c = b + 5
# print(c)
