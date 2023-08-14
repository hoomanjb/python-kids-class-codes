# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# [('g', 2), ('o', 3)]


# def char_counter(text):
#     result = []
#     # text_to_list = []
#     # for item in text:
#     #     text_to_list.append(item)
#     # unique_char = set(text_to_list)
#     unique_char = set([item for item in text])
#     if not text:
#         return result
#     for item in unique_char:
#         counter = 0
#         for inner_item in text:
#             if item == inner_item:
#                 counter += 1
#         result.append((item, counter))

#     return result
#
#
# print(char_counter('google.com'))


# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc;lkfhjglkfsjhg', 'xyzsfdsfdsdf'
# Expected Result : 'xyc abz'

#  Write a Python function that takes two list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
# ['asda', 'asdadasd', 'qweqew']
# ['aaaa', '1adadsads', 'adsasdadsadsa']

# a = ['asda', 'asdadasd', 'qweqew']
# b = ['aaaa', '1adadsads', '243243243234']
#
#
# def find_largest_word(a, b):
#     bozorge_avali = ''
#     for item in a:
#         if len(item) > len(bozorge_avali):
#             bozorge_avali = item
#
#     bozorge_dovomi = ''
#     for item in b:
#         if len(item) > len(bozorge_dovomi):
#             bozorge_dovomi = item
#
#     if len(bozorge_avali) > len(bozorge_dovomi):
#         return bozorge_avali, len(bozorge_avali)
#     elif len(bozorge_avali) == len(bozorge_dovomi):
#         return False
#     else:
#         return bozorge_dovomi, len(bozorge_dovomi)
#
#
# print(find_largest_word(a, b))


# Write a Python program to sum all the items in a list.
# [4, 6, 1, [9, 11], 3, 5, 7, 2, 7, 'ok' , 2, 'salam']

# def my_list_sum(my_list):
    # result = 0
    # for item in my_list:
    #     if isinstance(item, int) or isinstance(item, float):
    #         result += item
    # return result
#     result = 0
#     for item in my_list:
#         try:
#             result += item
#         except Exception as ex:
#             print(ex)
#     return result
#
#
# a = [4, 6, 1, [9, 11], 3, 5, 7, 2, 7, 'ok' , 2, 'salam', 9.56]
# print(my_list_sum(a))

# a = 'salam'
# print(isinstance(a, list))

# ###############################################3
# Dict - key - value

# my_user = {
#     'name': 'anisa',
#     'age': 52,
#     'address': ['tehran', 'iran']
# }
# print(my_user['name'])
# print(my_user['address'])
# a = [5, 9, 11]
# b = dict(a)


# my_dict = {
#     'name': 'anisa',
#     'age': 52,
#     'address': ['tehran', 'iran']
# }

# print(my_dict.pop('aa'))
# print(my_dict)
# print(my_dict.values())
# print(type(my_dict.values()))

# print(my_dict.keys())
# print(my_dict.items())

# for key, value in my_dict.items():
#     print(key, value)

# print(my_dict['aaa'])
# print(my_dict.get('aaa', False))
# print(my_dict.popitem())
# print(my_dict)
# print(my_dict.update({'email': 'test@gmail.com', 'age': 99}))
# print(my_dict)


# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 1, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# def char_counter(text):
#     result = {}
#     for item in text:
#         value = result.get(item)  # item = 'g'
#         if not value:
#             value = 0
#         result.update({item: value + 1})
#     return result
#
# print(char_counter('google.com'))

# Write a Python script to concatenate the following dictionaries to create a new one.
#
# Sample Dictionary :
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# result = {}
# for item in (dic1, dic2, dic3):
#     result.update(item)
# print(result)