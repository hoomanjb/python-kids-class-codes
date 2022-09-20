# dictionary - ordered , changeble , not duplicate
#
name = 'hooman'
my_dict = {
    'name': None,
    'age': 30,
    'email': 'test@gmail.com',
    'addrees': ['tehran', 'karaj'],
    0: 'test',
    123: 'test2'
}

# print(my_dict)
# print(my_dict['name'])
# print(my_dict['addrees'])
# print(my_dict[0])
# print(my_dict.keys())
# print(my_dict.values())

# print(my_dict['chert'])
# print(my_dict.get('chert'))
#
# if not my_dict.get('chert'):
#     print('peyda nakardam')
# else:
#     print('peyda shod')

# print(my_dict)
# my_dict['name'] = 'salam'
# print(my_dict)
# my_dict['phone'] = 3216543
# print(my_dict)

# if 'test' in my_dict.values():
#     print('ok')
# else:
#     print('nis!!!!')


# for item in my_dict.items():
#     print(item)

# for key, value in my_dict.items():
#     print(key, value)

# for key, value in my_dict.items():
#     print(key, '###', value)

# a = {'phone': 123}
#
# my_dict.update(a)
# print(my_dict)
# print(my_dict)
# my_dict.pop('name')
# print(my_dict)


# a = {165, 456, 887, 123, 5543, 123, 554, 3, 55, 1, 2, 5, 7, 8, 3, 4, 11, 44}
# b = {4443, 3, 55, 1, 2, 5, 7, 8, 3, 4, 11, 44}
#
# print(a)
# print(b)

# ################################################3
# switch- case
# match - case
# if elif else

# age = input('plz enter age: ')
# match age:
#     case range(9, 15):
#         print('ok')
#     case range(15, 20):
#         print('ok2')
#     case range(20, 30):
#         print('ok3')
#     case _:
#         print('ok4')

# if a == 'hooman':
#     print('ok')
# elif a == 'test':
#     print('ok2')
# elif a == 'salam':
#     print('ok3')
# else:
#     print('ok4')
# ################################################

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
# my_dict = {'1': 2, '3': 4, '4': 3, '2': 1, '10': 0}
#
# values = my_dict.values()
# keys = my_dict.keys()
#
# print(values)
# print(keys)
#
# result = []
# for item in values:
#     if result == []:
#         result.append(item)
#     else:
#         for i in result:
#             if item <= i:
#                 index = result.index(i)
#                 result.insert(index - 1, item)
#             else:
#                 result.append(item)
#                 break
# print(result)

# Bubble Sort
# Selection Sort
# Insertion Sort

# ###################################
# 3. Write a Python script to concatenate following dictionaries to create a new one
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# result = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# result = {}
# for item in (dic1, dic2, dic3):
#     result.update(item)

# print(result)
# #############################################
# Write a Python script to check whether a given key already exists in a dictionary.


# a = 'name'
# if a in my_dict:
#     print('ok')

# ##############################################

# Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ######################################################
# Write a Python script to print a dictionary where
# the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# ########################################################
# Write a Python script to merge two Python dictionaries.
# #################################################3
# Write a Python program to sum all the items in a dictionary.
# sum = key - sum values
# ##############################################3333
#  #
# 11. Write a Python program to multiply all the items in a dictionary.
#
# 12. Write a Python program to remove a key from a dictionary.
#
# 13. Write a Python program to map two lists into a dictionary.
# a = [1, 2, 3, 4]
# v = [5, 6, 7, 8]
#
# 14. Write a Python program to sort a given dictionary by key.
#
# 15. Write a Python program to get the maximum and minimum value in a dictionary.
#
# 17. Write a Python program to remove duplicates from Dictionary.
#
# 18. Write a Python program to check a dictionary is empty or not.
#
# 19. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# 20. Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
#
# 21. Write a Python program to create and display all combinations
# of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
#
# 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.








