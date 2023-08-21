# lambda - function
# x = lambda a: a * 5
# print(type(x))
# print(x(10))

# def yechizi(a):
#     return a * 5
#
# z = yechizi
# print(z(10))
# x = yechizi(10)


# y = lambda a, b: a * b
#
# print(y(5, 9))


my_dict = {'a': 150, 'b': 250, 'c': 5, 'd': 900, 'e': 25}
# result = {'c': 5, 'e': 25, 'a': 150, 'b': 250, 'd': 900}

# a = []
# for index, value in enumerate(my_dict.values()):
#     a.append((index, value))
#
# print(a)

# a = [4, 5, 1, 2, 'h', 'a', 0, 11, 'hello']
#
# for index, item in enumerate(a):
#     print(index, item)

# unsorted = [4, 6, 2, 4, 6, 7, 8, 88, 88, 20, 1, 99, 200, 1, 29, 6, 33, 22, 999, 90, 78]
# result = []
# for item in unsorted:
#     if len(result) == 0:
#         result.append(item)
#     else:  # [1, 2, 2, 2, 2] -> 3
#         for index, inner_item in enumerate(result):
#             if item <= inner_item:
#                 result.insert(index, item)
#                 break
#             else:
#                 if inner_item == result[-1]:
#                     result.append(item)
#                     break
#
# print(result)


# unsorted = [4, 6, 2, 4, 6, 7, 8, 88, 88, 20, 1, 99, 200, 1, 29, 6, 33, 22, 999, 90, 78]
# result = []
#
# for item in unsorted:
#     inserted = False
#     for index, inner_item in enumerate(result):
#         if item <= inner_item:
#             result.insert(index, item)
#             inserted = True
#             break
#     if not inserted:
#         result.append(item)
#
# print(result)

# def insert_sorted(lst, item):
#     for index, inner_item in enumerate(lst):
#         if item <= inner_item:
#             lst.insert(index, item)
#             return
#     lst.append(item)
#
# unsorted = [4, 6, 2, 4, 6, 7, 8, 88, 88, 20, 1, 99, 200, 1, 29, 6, 33, 22, 999, 90, 78]
# result = []
#
# for item in unsorted:
#     insert_sorted(result, item)
#
# print(result)


# ############################
# tkinter

# sang kaghaz gheychi
# Start Game
# esmeto begoo:
# hatman horofe alefba bayad bezanam
#
# ######### Main Menu ##########
# UserName: hooman    ##########
# 1- start game
# 2- show score
# 3- restart game
# 4- edit name
# 5- exit
# ############################

# 1-
# ##############
# 1-sang 2-kaghaz 3-gheychi 4-back-to-main-menu
# barande shodi
# 1- edame bedi 2-back-to-main-menu


# ##############
# user = 0 - ai= 0
# ##############


# restart-game -> score 0


# function bashe



# my_dict = {'a': 150, 'b': 250, 'c': 5, 'd': 900, 'e': 25}
# a = sorted(my_dict.items(), key=lambda x: x[1])
# print(a)
#
# for item in my_dict.items():
#     print(item)

