# format string ->  f'' (new)  - ''.format
# a = 'Anisa'
# b = '20'
# text = f'{a} {b}'
# text = '{name} {age} {name} {name} {age} {age}'.format(name=a, age=b)
# print(text)

# ######################################

# a = 10
# b = 'anisa'
# name = input('lotfan yek esm vared konid: ')
# age = input('enter your age: ')
# print(a)
# print(b)

# ##########################################
# List  - (ordered - changeable - allow duplicate value)
# my_list = [3, 5, 7, 'hello', 0, 'world', [99, 10], 88, [4, 5, [100, 200], 'SZV'], 'anisa']

# print(my_list[0])
# print(my_list[-1])
# print(my_list[2:7])
# print(len(my_list))
# print(my_list[8][1])
# print(my_list[8][2][1])
# print(my_list[8][3][2])

# iterable -> قابل شمارش list
# my_list = [3, 5, 2, 6, 2]
# my_list[1] = 7
# print(my_list)
# my_list[1:4] = [10, 11, 12]
# print(my_list)

# my_list = [5, 7, 9, 10]
# print('a' in my_list)
# name = 'anisa'
# print('z' in name)

# #######################################
# دستورهای کنترلی
# شرط - انتخاب
# if - match

# a = 10
# b = 7
# # condition - expression - body
# if a < b:
#     print('a az b koochik tar ast!!!!')
# else:
#     print('a az b koochaktar nis!!!')
# print('injaaaaaaa')



# a = 10
# b = 7
# c = 2
# # condition - expression - body
# if a < b:
#     print('a az b koochik tar ast!!!!')
# elif b > c:
#     print('b az c bozorgtare')
# elif c > a:
#     print('b az c bozorgtare')
# else:
#     print('a az b koochaktar nis!!!')
# print('injaaaaaaa')

# a = 10
# b = 7
# if a > b or a > 15:
#     print('ok')
# if a == 10:
#     print('ok')
# print('harchi shod!')

# True  1  4  ' ' [2]
# False 0 '' []

# if 1:
#     print('ok')


# a = 10
# b = 5
# if a < b:  # اگر آ از ب کوچکتر بود یکاری بکن یعنی آ از ب حتما باید کوچکتر باشه
#     print('ok')
#
# if not a < b:  # اگر آ از ب کوچکتر نبود یکاری بکن یعنی آ ز ب بزرگت باشه یه مساوی باشه
#     print('ok')

# #################################################
# if - switch-case (سوییچ کیس همون ایف الس خودمونه)
# match-case

# a = 'hello'
# if a == 'salam':
#     print(1)
# elif a == 'Hi':
#     print(2)
# elif a == 'سلام':
#     print(3)
# elif a == 'hello':
#     print(4)
# else:
#     print(0)
#
# match a:
#     case 'salam':
#         print(1)
#     case 'Hi':
#         print(2)
#     case 'سلام':
#         print(3)
#     case 'hello':
#         print(4)
#     case _:
#         print(0)

# ######################################
# python 2 - 2.7 backward campatibility
# python 3 - 3.11
#

# ###################################
# ماشین حساب بنویسین جمع و ضرب و تفریق و تقسیم 2تا ورودی از کاربر بگیره
# اگر کاربر عدد نداد خطا بهش بده
