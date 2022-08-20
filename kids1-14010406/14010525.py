# sang kaghaz gheychi - best of 5
# import random
#
# my_list = ['sang', 'kaghaz', 'gheychi']
# user_score = 0
# pc_score = 0
#
#
# def how_is_winner(pc, user):
#     # result -> 0 = equal, 1 = pc, 2 = user
#     if pc == user:
#         return 0
#     elif pc == 'sang':
#         if user == 'kaghaz':
#             return 2  # user is winner
#         else:
#             return 1  # pc is winner
#     elif pc == 'kaghaz':
#         if user == 'gheychi':
#             return 2  # user is winner
#         else:
#             return 1  # pc is winner
#     else:
#         if user == 'sang':
#             return 2  # user is winner
#         else:
#             return 1  # pc is winner
#
#
# print('Game Is Started')
# chand_bar = int(input('chanbar mikhay bazi koni? '))
# for _ in range(chand_bar):
#     pc_choice = random.choice(my_list)
#     user_choice = input('select (sang - kaghaz - gheychi): ')
#     result = how_is_winner(pc_choice, user_choice)
#     print(f'PC choice is {pc_choice} and your choice is {user_choice}')
#     if result == 0:
#         print('Equal !!!')
#     elif result == 1:
#         print('Pc is Winner !!!')
#         pc_score += 1
#     else:
#         print('User is Winner')
#         user_score += 1
#
# print(50 * '#')
# print('Game Over')
# if pc_score > user_score:
#     print(f'PC is Winner with {pc_score} point.')
# elif pc_score < user_score:
#     print(f'User is Winner with {user_score} point.')
# else:
#     print(f'Equal with {user_score} point.')
# print(50 * '#')









