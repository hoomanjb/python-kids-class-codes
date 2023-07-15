# a = 2
#
# if a < 5:
#     print('1')
# elif a == 5:
#     print('2')
# else:
#     print('3')
#
#
# if a == 5:
#     print(4)

# ############################ #

# Loop -> (while , for)

# while -> zamani az while estefade mikonim k tedaad loop moshakhas nabashad
# for -> tedad moshakhas bashad


# password = '123'
# user_password = input('enter password: ')
#
# while password != user_password:
#     print('password is Wrong!')
#     user_password = input('enter password: ')
#
# print('Tamaaaaam!')

# a = 1
#
# while a <= 10000000000:
#     print(f'counter is: {a}')
#     a += 1  # a = a + 1
#
# print('Tamaam')


# a = 1
#
# while a <= 100:
#     if a % 2 == 0:
#         print(a)
#         if a == 50:
#             print('YEAAAAAAAy')
#     else:
#        pass
#     a += 1

# 1 True
# break , continue
# password = '123'
#
# while True:
#     user_password = input('enter password: ')
#     if password == user_password:
#         print('Welcome')
#         break
#     else:
#         print('password is Wrong!')
#
#
# print('Tamaaaaam!')


# a = 1
# while True:
#     print(a)
#     if a >= 1000:
#         break  # halghe ro mishkane va halghe tamam mishe
#     if a % 2 == 0:
#         print('zoj')
#         a += 2
#         continue  # halghe ro yeki mindaze jelo
#     else:
#         a += 1
#     print('harchiii')

# ###############################
# for

# my_list = [1, 2, 3, 4, 5]
#
# for item in my_list:
#     print(item)
#
# print('tamam')
#
#
# for item in range(1, 1001):  # [1,2,3,4,5,6 .... , 1000]
#     print(item)



# text = 'Salam'
#
# for item in text:
#     print(item)

# my_list = [[1, 2, 7], [3, 4], [5, 6, 10]]

# for item in my_list:
#     print(item)


# a, b, c = 1, 2, 3
# a= 1
# b= 2
# c =3

# *a, b, c = 1, 2, 3, 4, 6, 7, 45, 'salam'
# print(a)
# print(b)
# print(c)

# my_list = [[1, 2, 7], [3, 4], [5, 6, 10]]
#
# for item1, *item2 in my_list:
#     print(item1, item2)


# 1*1 1*2 1*3 1*4  ...    1*10

for a in range(1, 11):
    #a = 1
    #a = 2
    #a = 3
    for b in range(1, 11):
        print(a * b)
        # for c in range(1, 11):
        #     print(a, b)
        #     pass
    print('########################')

