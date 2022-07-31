a = 3
b = 10

# if a < b and a == 5:
#     print('a az b koochik tar ast va a == 5 ast')
# elif a == 3:
#     print('a == 3')
# elif a == 4:
#     print('a == 4')
# elif a == 7:
#     print('a == 7')
# else:
#     print('a az b koochik tar nis')

# ------------------------------------------
# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# a=1
#
# p=int(input("در ضرب چه عددی مشکل داری؟"))
# while a<10:
#     l = a * p
#     s=int(input(f'{a} * {p} ?'))
#     if s==l:
#         a += 1
#         if a == 10:
#             a = 1
#             p += 1
#             print("wow")
#     else:
#         print("noo ):")


# x = 1
# while x <= 10:
#     row = x
#     y = 1
#     my_list = []
#     while y <= 10:
#         col = y
#         my_list.append(x*y)
#         y += 1
#     print(my_list)
#     x += 1


# x = 1
# while x <= 10:
#     row = x
#     y = 1
#     my_string = ''
#     while y <= 10:
#         col = y
#         my_string += f'{x*y:*<4}'   # '5 10 15 20 ..... 50'
#         y += 1
#     print(my_string)
#     print()
#     x += 1

# x = 1
# while x < 10:
#     print(x)
#     x += 1

for x in range(1, 11):
    my_string = ''
    for y in range(1, 11):
        my_string += f'{x * y:<4}'
    print(my_string)
