# 1. Write a Python program to sum all the items in a list.
# print(sum(a))
# def my_sum(my_list):
#     result = 0
#     for item in my_list:
#         if isinstance(item, int) or isinstance(item, float):
#             result += item
#         # else:
#         #     print(f'{item} is not int or float')
#     return result
#
# a = [4, 7, 10, 34, 6, 88, 'salam', 44, 'hi', ['hello'], 0, 5.6, 9.9]
# b = my_sum(a)
# print(b)

# 2. Write a Python program to multiply all the items in a list.

# 3. Write a Python program to get the largest number from a list.

# print(max(a))
# def my_max(my_list):
#     largest = 0
#     for item in my_list:
#         if isinstance(item, int) or isinstance(item, float):
#             if item > largest:
#                 largest = item
#     return largest
#
# a = [4, 7, 10, 34, 6, 88, 'salam', 44, 'hi', ['hello'], 0, 5.6, 9.9]
# b = my_max(a)
# print(b)

# 4. Write a Python program to get the smallest number from a list.


# 5. Write a Python program to count the number of strings where
# the string length is 2 or more and the first and last character are same from
# a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# a = 'test'
# a[0] == a[-1]
# def my_function(my_list):
#     count = 0
#     for item in my_list:
#         if len(item) > 2 and item[0] == item[-1]:
#             print(item)
#             count += 1
#         # else:
#         #     print(item)
#     return count
# b = my_function(['abc', 'xyz', 'aba', '1221', 'test', 'aaaaz', '11231231', 'aa'])
# print(b)


# 6. Write a Python program to get a list, sorted in
# increasing order by the last element in each tuple
# from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def last(n):
#     return n[-1]
#
# def my_order(my_list):
#     return sorted(my_list, key=last)
    # for item in my_list:
# print(sorted([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
# b = my_order([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
# print(b)

# def my_order(my_list):
#     result = []
#     lasts = []
#     index = 0
#     for item in my_list:
#         lasts.append((index, item[-1]))
#         index += 1
#     # lasts.sort()
#     return result
#
# b = my_order([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
# print(b)


# def last(n):
#     return n[-1]
#
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

# #######################################################
# Set - unordered unchangeable not allow duplicate

# a = [2, 4, 5, 6, 7, 9, 9, 10, 11, 2]
# b = set(a)
# print(a)
# print(b)

# a = {3, 5, 7, 1, 4, 6, 8, 2, 4, 1, 5, 7}
# b = list(a)
# print(a)

# a = list(set([2, 4, 5, 6, 7, 9, 9, 10, 11, 2]))
# print(a)


# a = {3, 5, 7, 1, 4, 6, 8, 2, 4, 1, 5, 7, 'hello', (5, 1), (5, 1)}
# print(a)

# this_set = {"apple", "banana", "cherry", "apple"}
# for item in this_set:
#     print(item)
# print('apple' in this_set)
# this_set.add('havij')
# print(this_set)

# this_set = {"apple", "banana", "cherry", "apple"}
# tropical = {"pineapple", "mango", "papaya", 'apple'}

# this_set.update(tropical)
# print(this_set)
# this_set.remove('chert')
# print(this_set)
# this_set.discard('chert')
# print(this_set)

# this_set.pop()
# print(this_set)
# this_set.clear()

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
#
# print(set3)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# print(x.intersection(y)) # eshterak
# print(y.intersection(x))
# print(x.symmetric_difference(y)) # ejtema - eshterak
# print(x.difference(y)) # tafazol
# print(y.difference(x))

