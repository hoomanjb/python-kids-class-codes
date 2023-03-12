# Dictionary
# key: value
data = {'name': 'hooman',
        'age': 10,
        5: 'salam',
        'colors': ['red', 'blue', 'black'],
        'status': True
        }

# print(data)
# print(type(data))

# name = data['name']
# print(name)
# a = data['test']   ## in dg bara estefade khoob nis

# a = data.get('test')
# a = data.get('test', 'nabood')
# print(a)

# keys = data.keys()
# print(keys)
# values = data.values()
# print(values)

# data['status'] = False

# if 'test' in data.keys():
#     print('ok')
# else:
#     print('Wrong!')


# a = data.items()
# print(a)


# for item in data:
#     print(item)


# data = {'name': 'hooman',
#         'age': 10,
#         5: 'salam',
#         'colors': ['red', 'blue', 'black'],
#         'status': True
#         }

# for key, value in data.items():
#     print(f'key is {key} and value is {value}')  # format string


# a = {'new': 123}
# data.update(a)
# print(data)

# keys = ['a', 'b', 'c', 'd', 'e']
# values = [1, 2, 3, 4, 5]

# names = ['nik', 'katie', 'james']
# ages = [32, 31, 34]

# result = {}
# for key in names:
#     for value in ages:
#         result.update({key: value})
#         ages.remove(value)
#         break
# print(result)

# dictionary = dict(zip(names, ages))
# print(dictionary)

# ##################################### #

# data = {'a': 4, 'b': 1, 'c': 6, 'f': 9, 'g': 2}
# result = {'b': 1, 'g': 2, 'a': 4, 'c': 6, 'f': 9}

# data = {'a': 4, 'b': 6, 45: 3, 'salam': 13}
# result = sorted(data.values())
# print(result)

# data = {'a': 4, 'b': 1, 'c': 6, 'f': 9, 'g': 2}
# result = dict(sorted(data.items()))
# print(data)
#

# data = {
#     'a': 4,
#     'b': 1,
#     'c': 6,
#     'f': 9,
#     'g': 2
#     }
#
# a = data.values()
# result = sorted(a)
# keys = data.keys()
# print(f"{keys} : {result}\n") # \n = new line

# footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
#
# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
# print(sorted_footballers_by_goals)


# data = {'a': 4, 'b': 1, 'c': 6, 'f': 9, 'g': 2, 's': 2}
# sorted_values = sorted(data.values())  # Sort the values
# result = {}
#
# for value in sorted_values:
#     for key in data.keys():
#         if data[key] == value:
#             result[key] = data[key]
#
# print(result)

# ########################### #

# make password
# password chand raghami bashad?
# password horoofe bozorg dashte bashe ya na?
# password horoofe koochik dashte bashe ya na?
# password adad dashte bashe ya na?
# password special !@#$%^*&^() dashte bashe ya na?

# 10 - True - True - False - True
# asDFGas@#$


import random
import string

# print('khosh amadid b ramz saze foghe hooshmande anisa!!!')
#
# q1 = input('dooste aziz passwordi k mikhay chanta char bashe??')
# q2 = input('dooste aziz passwordi k mikhay az ina ABCDEFGHIJKLMNOPQRSTUVWXYZ dashte bashe??')
# q3 = input('dooste aziz passwordi k mikhay az ina abcdefghijklmnopqrstuvwxyz dashte bashe??')
# q4 = input('dooste aziz passwordi k mikhay az ina 0123456789 dashte bashe??')
# q5 = input('dooste aziz passwordi k mikhay az in !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ dashte bashe??')


# a = string.ascii_uppercase
# b = string.ascii_lowercase
# c = string.digits
# d = string.punctuation
# print(a)
# print(b)
# print(c)
# print(d)

# lkjhlk234@#$egflkj;lk

# ################################### #

# lambda
# فانکشن یه بار مصرف بدون اسم

# x = lambda a: a + 10
# print(x)
# print(x(5))
# print(x(10))
# print(x(20))

# x = lambda a, b: a * b
# print(x(3, 5))
# print(x(2, 6))
# print(x(2, 2))

# def func1(n):
#         return lambda a: a * n
#
# x = func1(3)
# print(x(6))
# print(x(7))

# data = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
# result = sorted(data.items(), key=lambda x: x[1])
# print(result)
# print(data.items())

# a = ('a', 2)
# print(a[1])