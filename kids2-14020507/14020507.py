# yek adad beyne 1 ta 50 entekhab beshe
# age paiin goft  -> balatar hads bezan
#

# import random
# goal = random.choice(range(1, 51))
# # print(goal)
# up, down = 50, 1
# while True:
#     user_input = input(f'yek adad beyne {down} ta {up} entekhab kon: ')
#     if str(goal) == user_input:
#         print('Doroste tamam...')
#         break
#     elif not user_input.isdigit():
#         print('Wrong input... select 1-50')
#     elif goal > int(user_input):
#         print('bala tar hads bezan!')
#         down = user_input
#     else:
#         print('paiin tar hads bezan!')
#         up = user_input


# print('1')
# print('2')
# print('3')
# print('4')
# print('5')
# print('6')
# print('7')
# print('8')
# print('9')
# print('10')
# print('11')

a = input('yek adad vared konid: ')
if not a.isdigit():
    print('Wrong')
else:
    print(5 / int(a))

# TypeError, ValueError, ZeroDivisionError