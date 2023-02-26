# loop (while , for)

# for -> count
# while ->

# counter = 0
# while counter <= 10:
#     print('hello', counter)
#     counter += 1

# while True:
#     user_input = input('plz enter anything you want...! ')
#     if user_input == 'exit' or user_input == '0':
#         print('by by')
#         break
#     else:
#         print(f'you said #### {user_input} ####')
#         continue
#         print('123123')
#
# print('THE END')

# ###################################
# List -> ordered - changeable - allow duplicate value

# my_list = ["apple", 10, 5, [6, 3, 7], 'hello', [9, 10, [8, 99, 100]], 'world']
# print(type(my_list))
# print(my_list[0])
# print(my_list[3][1])
# print(my_list[4][1])

# a = [5, 8, 2, 6, 9, 0, 3, 1]
# print(a)
# a.pop()  # drop last value from the list
# print(a)
# a.pop(0)  # drop value by index
# print(a)
# a.pop(15)

# a = [5, 8, 2, 6, 9, 0, 3, 1]
# print(a)
# a.remove(8)  # drop or remove by value
# print(a)
# a.remove('hello')

# a = [5, 8, 2, 6, 9, 0, 3, 1]
# print(a)
# a.sort()
# print(a)

# my_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# print(my_list)
# my_list.sort()
# print(my_list)

# a = [5, 8, 2, 6, 9, 0, 3, 1]
# print(a)
# a.sort(reverse=True)
# print(a)

# a = [5, 8, 2, 6, 9, 0, 3, 1]
# a.append('hello')
# a.append(56)
# a.append([10, 20, 30])
# print(a)

# a.insert(2, 'world')
# print(a)
#
# a.append([7, 8, 9])
# a.extend([7, 8, 9])
# print(a)
#
# a = [5, 8, 2, 6, 9, 0, 3, 1, 5]
# print(a.count(5))


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = ["apple", "banana", "mango"]
# result = []
# for item in fruits:
#     if 'a' in item:
#         result.append(item)
# print(result)

# result = [item for item in fruits if 'a' in item]  # list comprehension
# result = [x for x in range(10) if x < 5]
# result = [item.upper() for item in fruits]
# print(result)

#