# List
my_list = [3, 6, 10, 'hello', 'world', 8, 'test', [1, 2, [10, 11]]]
# a = 'hello'
# print(a[0])
# print(my_list)
# print(my_list[0])
# print(my_list[4])

# print(my_list[-1])
# print(my_list[0:3])
# print(my_list[:3])
# print(my_list[3:])
# print(len(my_list))
# my_list = [3, 6, 10, 'hello', ['hooman'], 'world', 8, 'test', [1, 2, [10, 11]]]
# print(my_list[7][2][0])
# print(my_list[7][2][1])
# print(my_list[4][0][3])
# print(len(my_list)) # index = len - 1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list[start:end:step]
# print(a)
# print(a[::])
# print(a[::3])
# print(a[::-1])


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'test']
# a.append(10)
# print(a)
# print('test' in a)

# #############################################
# if

# a = 7
# b = 7
#
# if a > b:
#     print('A Gt B')
# elif a == b:
#     print('A is Equal B')
# elif a == b:
#     print('A is Equal B')
# elif a == b:
#     print('A is Equal B')
# elif a == b:
#     print('A is Equal B')
# else:
#     print('A Lt B')
#
# print('Finally')

# a, b, c, d = 4, 7, 15, 10
#
# if a < b and b > d:
#     print(1)
# elif b < d or a > b:
#     print(2)
# else:
#     print('anything')

# True 1 3 ' ' [2]
# False 0 '' []

# a = 0
# if a:
#     print(1)
# else:
#     print(2)

# a = 'hello'
# if 'h' in a:
#     print(1)
# else:
#     print(2)

# #################################3

# first_name = input('plz enter your first name: ')
# last_name = input('plz enter your last name: ')
# age = input('plz enter your age: ')
# gender = input('plz enter your gender: (Male/Female) ')
# 10 <  1 *
# 10-30  10 ta *
# 30 >   20 ta *
# if gender == 'Male':
#     print(f'Hello Mr {first_name} {last_name}')
#     if int(age) < 10:
#         print('*')
#     elif int(age) >= 10 and int(age) < 30:
#         print(10 * '*')
#     elif int(age) >= 30:
#         print(20 * '*')
# elif gender == 'Female':
#     print(f'Hello Mrs {first_name} {last_name}')
#     if int(age) < 10:
#         print('*')
#     elif int(age) >= 10 and int(age) < 30:
#     # elif 10 <= int(age) < 30:
#         print(10 * '*')
#     elif int(age) >= 30:
#         print(20 * '*')
# else:
#     print('Wrong Input!')

# tab = 4 spaces

# a = 3
# if not a == 5:
#     print(1)
# else:
#     print(2)


# #####################################333
# Loop  While - For

# a = [2, 4, 5, 7, 8]
#
# for item in a:
#     print(item)
#
# print('Finaly')


name = 'Mzagzgiez'
for item in name:
    print(item)
    if item == 'z':
        print('Found Z')

print('Finaly')