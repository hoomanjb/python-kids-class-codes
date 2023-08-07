# name = 'first name'
# b = name.title()
# c = name.capitalize()
# print(b, c)
# name = 'first namet'
# print(name.count('z'))
# print(name.index('z'))  # dastoor khoobi nis
# print(name.find('z'))


# name = 'first namet      t lkjdhg ;l h;ksdf ;t t;lk j;lkskftu lkjshdlkf tlskjfgh jstfsl jhdfksj htt sdfultsj dfsjudtf stdf skjtfd '
# print(name.find('t', 5))

# print(name.count('t'))

# count = 0
# index = 0
# for item in name:
#     if item == 't':
#         count += 1
#         print([count, index])
#     index += 1


# name = '         Anisa'
# print(name.center(2))
# print(name.endswith('?'))
# print(name)
# print(name.lstrip())
# print(name)
# print(name.rstrip())
# name = '                   Anisa          '
# name = name.lstrip()  # faghad chap
# name = name.rstrip()  # faghad rast
# name = name.strip()  # 2taraf baham

# name = 'Anisa'
# print(name.join(['@#', '12', 'ty']))
# a = ['firstName', 'LastName', 'email']
# print('#'.join(a))


# Regex - Regular Expression
# first-name
# FirstNAme
# fName
# name (U,L) - first
# @{gmail-yahoo}.com

# text = 'Fname Address Email Phone Age Lname'
# fullName = 'Hooman#JavanBakht'
# print(fullName.split(sep='#'))
# print(text.split())


# name = "Anisas"
# print(name.replace('x', 'z', 5))
# #####################################
# Format String
# #####################################
# List
# Duplicate - changeable - ordered

# a = [3, 5, 6, 'hello', [7, 8]]
# print(type(a))

# my_list = [4, 6, 1, 2, 8, 9]
# print(my_list.append('100'))
# my_list.append(200)
# print(my_list)


# a = [1, 3, 5]
# b = a
# 1kg data memory
# b = a , 1kg data memory
# b sakhte nemishe -> deep copy - shadow copy
# print(a)
# print(b)
# a.append(15)
# print(a)
# print(b)
# b.append(9)
# print(a)
# print(b)

# a = [1, 3, 5]
# b = a
#
# c = [4, 5, 6]
# d = [4, 5, 6]
# print(id(a), id(b))
# print(id(c), id(d))

# import copy

# my_list = [4, 6, 1, 2, 0]
# a = [8, 9]
# my_list.append(a)
# print(my_list)
# b = [11, 22]
# my_list.extend(b)
# print(my_list)
# print(my_list.index('0'))  # b dard nemikhore
# print(my_list.count('1'))

# my_list.insert(10, 'hello')
# print(my_list)
# my_list.pop(10)
# print(my_list)
# my_list[1] = 'salam'

my_list = [4, 6, 1, 2, 0, 'ok']
# my_list.remove('ok')
# my_list.remove('hello')
# print(my_list)

# my_list = [4, 6, 1, 2, 0]
# my_list.sort(reverse=True)
# my_list.sort()
# print(my_list)

# def chert(harchi):
#     return harchi.lower()
#
# my_list = ['A', 'H', 'z', 'Ok', 'a']
# my_list.sort(key=chert)
# print(my_list)


def chert(harchi):
    global a
    print(a)
    return harchi.lower()

a = 10