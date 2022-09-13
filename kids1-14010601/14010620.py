# LOOP  While For
#
#
# a = 0
#
# while a < 50:
#     print('#' * 20)
#     if a % 2 == 0:
#         print(a)
#     else:
#         print('a adade farde')
#     print('#' * 20)
#     a += 1

# break  continue
# a = 0
# while a < 100:
#     if a == 50:
#         print('BREAK')
#         break
#     else:
#         print(a)
#     a += 1


# a = 0
# while a < 100:
#     if a % 2 == 0:
#         a += 1
#         print('Continue')
#         continue
#     else:
#         print(a)
#     a += 1


# while True:
#     phone = input('plz enter your phone number: ')
#     if phone.isdigit() and len(phone) == 11:
#         print('Mamnoon')
#         break
#     else:
#         print('eshteba vared kardi')

# #################################
# For


# name = 'hoosdflsjkdflskdhflskdjflskjdfhlskjdakjslkjsfsjkan'
# my_list = [2, 5, 6, 'hello', [9, 10]]
# # for item in name:
# #     print(item)
#
# for item in my_list:
#     print(item)

# ###################################################
# 2ta vorodi adad
# 1 amalgar + - * /
# natije
# mikhay edame bedi ya na : are , na exit

# while True:
#     adad1 = input('yek adad vared konid: ')
#     adad2 = input('adad dovom ra vared konid: ')
#     amalgar = input('amalgari k mikhayd ro vared konid (+-*/): ')
#     if amalgar == '+':
#         print(int(adad1) + int(adad2))
#     elif amalgar == '-':
#         print(int(adad1) - int(adad2))
#     elif amalgar == '*':
#         print(int(adad1) * int(adad2))
#     elif amalgar == '/':
#         print(int(adad1) / int(adad2))
#     else:  # % ** //
#         print('hamchin amalgari mojod nis1')
#
#     user_choice = input('aya doos dari edame bedi ya na: yes no')
#     if user_choice == 'yes':
#         continue
#     else:
#         print('ByBY')
#         break


# a = input('adad: ')
# print(type(a))
# b = int(a)
# print(type(b))
# int str float bool
# a = 3.5
# print(type(a))
# b = int(a)
# print(type(b))
# print(b)
# c = str(a)
# print(type(c))
# print(c)
# d = bool(a)
# print(type(d))
# print(d)

# Jadval Zarb  1ta 10
# (3*1) (3*2) (3*3) (3*4) () () () () (3*10)
# (4*1) (4*2)       (4*10)
# addadha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for x in addadha:
#     for y in addadha:
#         print(x*y)
#     print('#' * 20)

# addadha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for x in addadha:
#     res = []
#     for y in addadha:
#         res.append(x*y)
#     print(res)


# addadha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for x in addadha:
#     res = ''
#     for y in addadha:
#         res += '   ' + str(x*y)
#     print(res)


# name = input('enter your name: ')
# print(name)
# text = f'b web site ma khosh amadid mr/miss {name}'
# print(text)
# name = 'hooman'
# phone = '1236546'
# email = 'asdasd@gmail.com'
# text = f'name: {name}\n' \
#        f'phone: {phone}\n' \
#        f'email: {email}'
# text = f'name: {name}phone: {phone}email: {email}'
# text = f'''
# name: {name}
# phone: {phone}
# email: {email}
# '''
# print(text)


# tamrin
# 5ta soal az karbar
# doros javab dad +1 score
# eshteba 3 bar talash -1