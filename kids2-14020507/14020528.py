# a = ['asdwada', 'wadsda', 'sadranaderi']
# b = ['verva', 'dadaad', 'fdvfv']
#
#
# def lister(a, b):
#     bozorgavaly = ''
#     for item in a:
#         if len(item) > len(bozorgavaly):
#             bozorgavaly = item
#         bozorgdovomi = ''
#     for item in b:
#         if len(item) > len(bozorgdovomi):
#             bozorgdovomi = item
#     if len(bozorgdovomi) > len(bozorgavaly):
#         return bozorgdovomi, len(bozorgdovomi)
#     elif len(bozorgdovomi) == len(bozorgavaly):
#         return False
#     elif len(bozorgdovomi) > len(bozorgavaly):
#         return bozorgavaly, len(bozorgavaly)
#
# print(lister(a, b))

# ######################################
# Write a Python program to map two lists into a dictionary.

# c = dict(zip(keys, values))

# def zipper_list(keys, values):
#     result = {}
#     index = 0
#     unique_value = set()
#     for item in keys:
#         try:
#             if result.get(item):
#                 unique_value.add(values[index])
#             else:
#                 result.update({item: values[index]})
#             result.update({item: unique_value})
#         except IndexError as ex:
#             print(ex)
#             result.update({item: None})
#         index += 1
#     return result
#
# keys = ['key1']
# values = ['val1', 'val2', 'val3', 'val3']
# result = {'key1': {'val1', 'val2', 'val3'}}
# print(dict(zip(keys, values)))
# print(zipper_list(keys, values))
# a = {2, 3}
# a.update({5})
# a.add(6)
# print(a)

# over thinking

# #############################################

import random
import string

# make password
q1 = input('chand raghami bashad?')  # 10
q2 = input('horoofe bozorg dashte bashe ya na?')  # ok
q3 = input('password horoofe koochik dashte bashe ya na?')  # na
q4 = input('password adad dashte bashe ya na?')  # na
q5 = input('password special !@#$%^*&^() dashte bashe ya na?')  # ok

# password = []
# candidates = []
#
# if q2 in ['ok', 'yes', 'y', 'bale']:
#     candidates.extend(['A', 'B', 'C', 'Y', 'Z'])
#
# if q3 in ['ok', 'yes', 'y', 'bale']:
#     candidates.extend(['a', 'b', 'd', 'y', 'z'])
#
# if q4 in ['ok', 'yes', 'y', 'bale']:
#     candidates.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
#
# if q5 in ['ok', 'yes', 'y', 'bale']:
#     candidates.extend(['!', '@', '#', '$', '^'])
#
# for item in range(int(q1)):
#     password.append(random.choice(candidates))
#
# print(''.join(password))

# candidates = ''
# password = ''
# if q2 in ['ok', 'yes', 'y', 'bale']:
#     candidates += string.ascii_uppercase
# if q3 in ['ok', 'yes', 'y', 'bale']:
#     candidates += string.ascii_lowercase
# if q4 in ['ok', 'yes', 'y', 'bale']:
#     candidates += string.digits
# if q5 in ['ok', 'yes', 'y', 'bale']:
#     candidates += string.punctuation
#
# for item in range(int(q1)):
#     password += random.choice(candidates)
#
# print(password)

# lambda - function

# Write a Python program to sort a given dictionary by key
# Write a Python program to get the maximum and minimum values of a dictionary.
# Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':-300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 100})

# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}