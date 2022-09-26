# a = [1, 3, 5, 7]
# print(a[2])
# name = ['a', 'b', 'c']
# phone = [1, 2, 3]
# address = ['g', 'h', 'i']
#
# my_dict = {'name': name, 'phone': phone, 'address': address}
#
# print(my_dict['name'])
#
# print(my_dict['phone'])
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# ####################################3
# 19. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400, 'z': 10}
#
# result = {}
#
# for key, value in d1.items():
#     for key2, value2 in d2.items():
#         if key == key2:
#             result.update({key: value + value2})
#             break
#
# for key2, value2 in d2.items():
#     if not result.get(key2):
#         result.update({key2: value2})
#
# for key, value in d1.items():
#     if not result.get(key):
#         result.update({key: value})
#
# print(result)

# #####################################################

# Function
# def my_sum(a, b):
#     c = a + b
#     print(c)
#     print('harchi')
#
# my_sum(7, 10)
# d = my_sum(9, 17)
# print(d)

# Optional Argument - voroodi del bekhah
# Required Argument - vorodi ejbarie tabe
# def my_function(first_name, last_name, phone=0):
#     print(phone)
#     return first_name + last_name

# positional Parameter
# keyword Parameter

# print(my_function(6, 10, 8))  # positional Parameter
# print(my_function(6, 10))  # positional Parameter
# print(my_function(first_name=2, last_name=40))  # keyword Parameter
# print(my_function(first_name=2, last_name=6, phone=1))



# def my_function(addad1, addad2, phone=123):
#     return int(addad1) + int(addad2)

#
# def my_sum(addad1: int, addad2: int, phone: str = '123456') -> str:
#     return str(addad1 + addad2)
#
#
# a = input('phone')
# if a.isdigit():
#     print(my_sum(addad1=int(a), addad2=10))
# else:
#     print('chert gofti')

# a = 'salam'
# print(a.__class__)
# print(type(a))
#
#
# class anisa:
#     def __add__(self, other):
#         return 10 * other


# a = 3 + 1
# print(a)

# a, b, *c = 10, 11, 12, 234, 456
#
# def my_function(a, *args):
#     result = 0
#     print(args)
#     print(type(args))
#     for item in args:
#         result += item
#     return result
#
# print(my_function(10, 20, 40, 12, 45, 5, 6, 1, 3, 6))


def my_function(a, b, *args, **kwargs):
    print(kwargs)
    print(args)
    return a + b

print(my_function('salam', 'hooman', 99))