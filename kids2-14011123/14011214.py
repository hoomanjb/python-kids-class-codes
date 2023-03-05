# deep copy va shallow copy

# from copy import deepcopy, copy
# shallow copy = copy

# A = [4, 6, 7]
# B = A
# print(A)
# print(B)
# A.append(9)
# print(A)
# print(B)
# B.append(10)
# print(A)
# print(B)
#
# C = deepcopy(A)
# print(A)
# print(B)
# print(C)
#
# A.append(15)
# print(A)
# print(B)
# print(C)

# ######################################## #
# Tuple - (ordered, unchangeable, allow duplicate value)

# my_tuple = ("apple", "banana", "cherry", "apple", 10, 20, [7, 9])
# a = tuple(("apple", "banana", "cherry", "apple", 10, 20, [7, 9]))
# print(my_tuple[0])
# print(my_tuple[-1])
# print(len(my_tuple))
# a = [7, 9]
# a[1] = 15
# print(a)

# my_tuple[0] = 22
# print(my_tuple)

# print(my_tuple)
# my_tuple = list(my_tuple)
# my_tuple[0] = 22
# my_tuple = tuple(my_tuple)
# print(my_tuple)

# my_tuple = ("apple", "banana", "cherry", "apple", 10, 20, [7, 9])
# print(my_tuple.count("apple"))
# print(my_tuple.index("apple"))

# خروجی داده های دیتابیس - ورودی دیتاها از فرانت وب سایت - ارسال دیتا

my_tuple = ("apple", "banana", "cherry", "apple", 10, 20, [7, 9])

# if "apple" in my_tuple:
#     print('ok')
#
# for item in my_tuple:
#     print(item)

# a, b, c = 1, 2, 3

# *a, b, c = ("apple", "banana", "cherry", "apple", 10, 20, [7, 9])
# print(a)
# print(b)
# print(c)

# #################################### #
# Set - (unordered - unchangeable - not allow duplicate values)
# سریع - تکراری هارو حذف میکنه - ترتیبم نداره
# A = {9, 7, 1, 2, 3, 4, 5, 5, 5}
# B = {2, 7, 11, 15, 20}
# print(A)
# print(A[0])
# print(A)
# print(B)
# A.add(99)
# print(A)
# A.remove(99)
# print(A)
# A.remove(100)
# print(A)
# A.discard(100)
# print(A)

# a = [4, 5, 4, 4, 1, 2, 3, 6, 7, 1, 4]
# print(a)
# a = list(set(a))
# print(a)
# list []  tuple ()  set {}
# set1 = {'A', 'B', 'C'}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)  # اجتماع
# print(set3)
# set1.update(set2)
# print(set1)


# set1 = {'A', 'B', 'C'}
# set2 = {1, 2, 3, 'A'}
# set4 = set1.intersection(set2)  # اشتراک
# print(set4)
# set1.intersection_update(set2)
# print(set1)

# set5 = set1.symmetric_difference(set2)
# print(set5)
# ####################################### #
# dictionaries
# collection
# data2 = ['anisa', 123, 'test@gmail.com', 222, 6345]

# data = {'name': 'anisa', 'phone': 1234, 'email': 'test@gmail.com'}
#
# print(data['name'])
# print(data['phone'])


# form = name - koemeli - phone - addres - email - blood - meliat -
# website -> front -> backend : {}


# Web
# server -> جایی که سایت قرار میگیره
# database ->  جایی که دیتاها قرار میگیرن و ذخیره میشن
# securiteis -> امنیت سایت
# designe -> دیزاین شکل و شمایل سایت
# frontend -> چیزی که سایت به کاربر نشون میده و رابط بین کاربر بک اند
# backend -> منطق پروژه

# static ->
# front -> anisa.shop -> http://anisa-api.shop/home/user data={'name': 'anisa', 'phone': 1234, 'email': 'test@gmail.com'}
# back -> anisa-api.shop -> database -> ok  anisa.shop/user data=ok
# API = Application Programmers Interface

# framework -> django - django-rest - fastAPI - .Net - Spring - Laravel
# request