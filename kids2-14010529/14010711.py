# Loop  ( While - For )
# while -> nadoonim daghighan chanbar tekrar she
# for  ->  midoonim chanbar gharare tekrar she
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(range(1000))

# for item in range(1000):
#     print(item)

# my_dict = {'name': 'hooman',
#            'phone': 123,
#            'address': ['a', 'b'],
#            'age': 5}

# for item in my_dict.values():
#     print(item)

# for key, value in my_dict.items():
#     print(key + ' ----', value)

# a = input()
# name = 'Anisalaksjdhlaskjdhalkshdlasdkj%a;ksjdhakjsdhlak%aklsnd;ka%ks;ljhflksjdbfhls%akjsdflksj%g'
# count = 0
# index = 0
# index_list = []
# result = {'count': 0, 'index_list': []}
# for item in name:
#     if item == '%':
#         count += 1
#         index_list.append(index)
#         result['count'] += 1
#         result['index_list'].append(index)
#     index += 1
# print(count)
# print(index_list)
# print(result)

# name = 'Anisalaksjdhlaskjdhalkshdlasdkj%a;ksjdhakjsdhlak%aklsnd;ka%ks;ljhflksjdbfhls%akjsdflksj%g'
# result = {'count': 0, 'index_list': []}
# for index, item in enumerate(name):  # ham item ro barmigardoone va ham index
#     if item == '%':
#         result['count'] += 1
#         result['index_list'].append(index)
# print(result)
# flag = True
# while flag:
#     phone = input('enter your phone number: ')
#     if phone.isdigit() and len(phone) == 11 and phone.startswith('09'):
#         print('ok merc')
#         flag = False
#     else:
#         print('wrong Input')

# flag = True
# while flag:
#     phone = input('enter your phone number: ')
#     if phone.isdigit():
#         if len(phone) == 11:
#             if phone.startswith('09'):
#                 print('4- ok merc')
#                 flag = False
#             else:
#                 print('3- bayad ba 09 shoro shode')
#         else:
#             print('2- bayad 11 ta adad bashad')
#     else:
#         print('1- bayad az adad ha estefade koni')

# while True:
#     phone = input('enter your phone number: ')
#     if phone.isdigit():
#         if len(phone) == 11:
#             if phone.startswith('09'):
#                 print('4- ok merc')
#                 break
#             else:
#                 print('3- bayad ba 09 shoro shode')
#         else:
#             print('2- bayad 11 ta adad bashad')
#     else:
#         print('1- bayad az adad ha estefade koni')


# for item in range(1, 1001):
#     if item % 2 == 0:
#         print(item)
#         continue
#         print(10 * '#')
#     print(10 * '#')

# session = True
# while session:
#     phone = input('enter your phone number: ')
#     if phone.isdigit():
#         if len(phone) == 11:
#             if phone.startswith('09'):
#                 print('4- ok merc')
#                 session = False
#             else:
#                 print('3- bayad ba 09 shoro shode')
#         else:
#             print('2- bayad 11 ta adad bashad')
#     else:
#         print('1- bayad az adad ha estefade koni')
# else:
#     print('Data base Baste shode moshkeli pish amade')

# for item in range(10):
#     print(item)
# else:
#     print('tamam shod')


# ########################################################333
my_dict = {'name': 'hooman',
           'age': 12,
           'address': ['1', '2']
           }

# print(my_dict)
# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.items())
# a = {'jadid': 123}
#
# my_dict.update(a)
# print(my_dict)
# a = {'age': 45}
# my_dict.update(a)
# print(my_dict)
# my_dict['age'] = 67
# print(my_dict)

# print(my_dict['harchi'])
# print(my_dict.get('harchi'))
# print('injaaaaaaaaaaaaa')

# my_dict.pop('age')
# print(my_dict)
# my_dict.clear()
# print(my_dict)


# ##########################################################
# function - tabe

# def my_function():
#     return 'salam'
#
# a = my_function()
#
# print(a)


# def my_function():
#     print('salam')
#
# my_function()

# Required Args
# Optional Args
# def my_function(addad1: int, addad2: int, flag: bool = True):
#     c = addad1 + addad2
#     return c
#
# # Positional Parameter
# # Keyword Parameter
# a = my_function(addad1=5, addad2=7, flag=False)
# print(a)


# def my_function(a, b, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     result = 0
#     for item in args:
#         result += item
#     return a + b, result
#
# s, v = my_function(4, 7, 10, 11, 43, name='hooman', age='20')
# print(s)
# print(v)



