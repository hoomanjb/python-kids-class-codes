# text = 'Welcome {} to our website'
# name = input('enter your name: ')
# result = 'Welcome ' + name + ' to our website'
# print(result)

# Format String - fstirng

# name = input('enter your name: ')
# name, age, class_name = 'Hooman', 20, 'Python'
# text = 'Welcome {user_name} to our website. your age is: {user_age} and your class is: {user_class}'
# result = text.format(user_name=name, user_age=age, user_class=class_name)
# print(result)

# name, age, class_name = 'Hooman', 20, 'Python'
# text = f'Welcome {name} to our website. your age is: {age} and your class is: {class_name}'
# print(text)

# ###########################################
# List -> Sequence دنباله
# index
# قابل تغییرن
# اجازه ی مقدار تکراری

my_list = [2, 3, 5, 'hello', 'a', '1', 2, 5, 'a', [9, 10], 50, ['ok', 'test', 50]]
# print(type(my_list))
# print(my_list)

# print(len(my_list))
# print(my_list[0])
# print(my_list[1])
# print(my_list[3])
# print(my_list[1:6:2])
# print(my_list[-1])
# print(my_list[-3])
# print(my_list[-1][1])

my_list = [2, 3, 5, 'hello', 'a', '1', 2, 5, 'a', [9, 10], 50, ['ok', 'test', 50]]
# print(my_list[-1])
# a = my_list[-1]
# print(a[1])
# print(my_list[:-1])

# b = a[1]
# print(b)
# print(b[2])

# print(my_list[-1][1][2])
# print(my_list)
# my_list[1] = 'salam'
# print(my_list)

# my_list = my_list + [77]
# print(my_list)

# print(my_list)
# my_list[:4] = [99, 88, 77, 66]
# print(my_list)

# a = [20]
# print(a * 5)
# #################################
# if - conditions
# a = 20

# if a > 5 and a == 10:
#     print('a az 5 bozorg tar ast.')
#     print(1)
#     print(2)
#     print(3)
#
# print('harchi!!!')




# a = 5
# b = 7
#
# if a > 10:
#     print(1)
# elif a == 4:
#     print(2)
# elif a == b:
#     print(3)
# else:
#     print(4)
#
# if a > b:
#     print(1)
# else:
#     print(2)

# 1 True 's' ' ' [1]
# 0 False  '' []

# if True:
#     print(1)
#
# if 1:
#     print(10)
#
# if ' ':
#     print('ok')
#
# if 0:
#     print(100)
#
# if '':
#     print(200)


# name = 'Hooman'
#
# if 'Z' in name:
#     print(1)
# elif name == 'salam':
#     print(2)
# elif 'H' not in name:
#     print(3)
# else:
#     print(4)

# switch - case

# name = 'Hooman'
#
# match name:
#     case 'salam':
#         print(1)
#     case '1':
#         print(2)
#     case 'hooman':
#         print(3)
#     case _:
#         print(4)
#
# if name == 'salam':
#     print(1)
# elif name == '1':
#     print(2)
# elif name == 'hooman':
#     print(3)
# else:
#     print(4)


# name - age - email
# 10-15 -
# 15-25 -
# > 25  -