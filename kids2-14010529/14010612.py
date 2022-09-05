# fisrt_name = input('enter your name: ')
# last_name = input('enter your last name: ')
#
# print(f'welcome {fisrt_name} {last_name} to the game!')
#
# while True:
#     menu_message = """
#     1 - jaam
#     2 - tafrigh
#     3 - zarb
#     4 - taghsim
#     5 - exit
# """
#     user_input = input('kodom? ')
#     if user_input == '5':
#         print('goodby')
#         break
#     elif user_input in ['1', '2', '3', '4']:
#         add1 = input('addad 1 :')
#         add2 = input('addad 2 :')
#         if not add1.isdigit() and not add2.isdigit():
#             print('adad doros bede!')
#             print()
#             continue
#         if user_input == '1':
#             print(int(add1) + int(add2))
#         elif user_input == '2':
#             print(int(add1) - int(add2))
#         elif user_input == '3':
#             print(int(add1) * int(add2))
#         else:
#             print(int(add1) / int(add2))
#
#     else:
#         print('eshtebah entkhab kardi!')
#         print()


# ################################################

# text = '{fname} - {lname} - {phone} - {email}'.format(
#     fname=1, lname=2, phone=3, email=4)

# {name:[[fill]align][sign][#][0][width][,][.precision][type]}
# a = '{jaye_khali:>10}'.format(jaye_khali='test')
# a = '{jaye_khali:^10}'.format(jaye_khali='testtttttttt')
# a = '{jaye_khali:^.10}'.format(jaye_khali='testttttthgvkhgvjhgvjhgvjgttt')
# a = '{jaye_khali:<10.5}'.format(jaye_khali='testttttttttttt')
# a = '{:d}'.format(23)
# a = '{:f}'.format(3.1432165498)
# a = '{:.2f}'.format(3.1432165498)
# a = '{:5.2f}'.format(3.1432165498)
# a = '{:02.2f}'.format(13444.143216549)
# a = '{:010.2f}'.format(3.143216549)




# {name:[[fill]align][sign][#][0][width][,][.precision][type]}
# config align = '^'
# a = '{jaye_khali:{align}{width}.{precision}}'.format(jaye_khali='test', align='^', width=10, precision='4')
# print(a)

# #############################################################3
# a = ['test', 1, 3, 7, [5, 'hello']]

# print(a)
# a.append([9, 7])
# a.extend([9, 7])
# print(a)
# print(a.index(3))
# print(a.index(25))
# a = ['test', 1, 3, 7, [5, 'hello']]
# a.index('hello')
# for item in a:
#     if isinstance(item, list):
#         print(item.index('hello'))

# a = ['test', 6, 3, 7, [5, 'hello'], 'test']
# a.insert(2, 'yechizi')
# print(a)
# a.remove('test')
# a.pop(2)
# for item in a:
#     if item == 'test':
#         a.remove('test')
# print(a)
# a = ['test', 6, 3, 7, [5, 'hello'], 'test']
# a[0] = 50
# print(a)
# b = []
# for item in a:
#     if not item == 'test':
#         b.append(item)
# print(b)

# a = [78, 6, 3, 7, 1, 6]
# thislist = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
# # code ascii
# thislist.sort()
# print(thislist)
# thislist.sort(key=str.lower)
# print(thislist)

