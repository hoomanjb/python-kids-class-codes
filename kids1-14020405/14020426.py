# for a in range(1, 11):
#     radif = ''  # 1, 1 2 , 1 2 3
#     for b in range(1, 11):
#         radif = radif + f'{a*b:3}' #  radif = (radif + 1*1) = 1,  (radif + 1*2) , radif + 1*3
#     print(radif)
    # print(type(radif))
    # print('########################')


# ################################################ #
# s1 = 'javabe 2 + 2 che mishavad? a)4  b)5 '
# s2 = 'por sorat tarin net jahan bara kojas? a)IR  b)USA '
# s3 = 'bozorgtarin heyvan khoshki? a)fill b)gorbe '
#
# score = 0
#
# for item in range(3):
#     javab1 = input(s1)
#     if javab1 in ['a', '4']:
#         print('Afarin...')
#         score += 1
#         break
#     else:
#         print('eshtebah gofti bishtar deghat kon.')
#
# for item in range(3):
#     javab2 = input(s2)
#     if javab2 in ['a', 'IR']:
#         print('Afarin...')
#         score += 1
#         break
#     else:
#         print('eshtebah gofti bishtar deghat kon.')
#
#
# for item in range(3):
#     javab3 = input(s3)
#     if javab3 in ['a', 'fill']:
#         print('Afarin...')
#         score += 1
#         break
#     else:
#         print('eshtebah gofti bishtar deghat kon.')
#
# print('bazi tamoom shod. khaste nabashi')
# print(f'emtiaze shoma shode: {score}')


# ###################################################3
# function - تابع

# print(5*5)
# print('salam chetori')
# a = input('enter: ')
# a = range(10)
# a = '{}'.format('salam')

# def my_function(a, b):  # 2ta parameter
#     c = (a*b) + 10
#     return c
#
# # s = input('addad1: ')
# # v = input('addad2: ')
# result = my_function(7, 4)  # 2ta arguments
# print(result)


# def func2(a, b):
#     c = a + b + 10
#     print(c)
#
# result = func2(7, 9)
# print(result)

# tavabe mitavanand khoorooji nadashte bashan. print()
# tavabe mitavannad vooroodi ham nadashte bashan. session()

# def welcome():
#     print('Welcome!!!')
#     print('Turn on!')


# def func2():
#     return 4, 5, 'salam'
#
#
# a, b, c = func2()
# print(a)
# print(b)
# print(c)

# f = 15
#
# def func3(a):
#     b = a * 5 + 7
#     c= 15
#     d=40
#     print(f)
#     return b
#
# result = func3(4)
# print(result)



def check_asnwer(soal, javab, emtiaz):
    for item in range(3):
        user_input = input(soal)
        if user_input in javab:
            print('Afarin...')
            emtiaz += 1
            break
        else:
            print('eshtebah gofti bishtar deghat kon.')
    return emtiaz
#
# s1 = 'javabe 2 + 2 che mishavad? a)4  b)5 '
# s2 = 'por sorat tarin net jahan bara kojas? a)IR  b)USA '
# s3 = 'bozorgtarin heyvan khoshki? a)fill b)gorbe '
#
# score = 0
# score = check_asnwer(s1, ['a', '4'], score)
# score = check_asnwer(s2, ['a', 'IR'], score)
# score = check_asnwer(s3, ['a', 'fill'], score)
# print(score)

# agar karbar baaade 3bar natoonest javab bede nomre manfi begire

# bazi sang kaghaz gheychi
# 10 dast bazi konid
# karbar ye ai
# chek konid ki barande shode
# harki brande shode bood 1 emtiaz begire
# baade 10 dast natije koli ro begi
# user 4 va ai 4 va 2 mosavi


import random
a = ['s', 'k', 'g']
print(random.choice(a))


