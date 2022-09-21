# name?

# 1- start bazi
# 2- namayeshe emtiazha
# 3- edit info
# 4- exit
import random

#
# def getting_name(new):
#     if new:
#         message = 'plz enter your name: '
#     else:
#         message = 'plz enter your new name for edit: '
#     name = input(message)
#     return name
#
#
# def show_scores():
#     print(40 * '*')
#     print(f'emtiaze user is: {user_score}')
#     print(f'emtiaze ai is: {ai_score}')
#     print(40 * '*')
#
#
# def who_is_winner(user, ai):
#     # return 0 -> mosavi
#     # return 1 -> user is winner
#     # return 2 -> ai is winner
#     if user == ai:
#         return 0
#     elif user == "sang":
#         if ai == "gheychi":
#             return 1
#         else:
#             return 2
#     elif user == "kaghaz":
#         if ai == "sang":
#             return 1
#         else:
#             return 2
#     elif user == "gheychi":
#         if ai == "kaghaz":
#             return 1
#         else:
#             return 2
#
#
# def set_score(winner):
#     if winner == 0:
#         print('Mosavi shodid')
#     elif winner == 1:
#         print('shoma barande shodidi!')
#         global user_score
#         user_score += 1
#     else:
#         print('ai barande shode!')
#         global ai_score
#         ai_score += 1
#
#
# def start_game():
#     user_choice = input("enter sang kaghaz gheychi")
#     possible_choice = ["sang", "kaghaz", "gheychi"]
#     ai_choice = random.choice(possible_choice)
#     if user_choice in possible_choice:
#         winner = who_is_winner(user_choice, ai_choice)
#         set_score(winner)
#     else:
#         print('Wrong Input!!!')
#     show_menu()
#
#
# def show_menu():
#     print(40 * '*')
#     print(f'User-name: {user_name}')
#     print(40 * '*')
#     text = """MENU:
# # 1- start bazi
# # 2- namayeshe emtiazha
# # 3- edit info
# # 4- exit
# """
#     print(text)
#     user_input = input('? ')
#     check_input(user_input)
#
#
# def check_input(user_input):
#     if user_input == '1':
#         start_game()
#     elif user_input == '2':
#         show_scores()
#     elif user_input == '3':
#         getting_name(False)
#     elif user_input == '4':
#         print('ByBY')
#         return False
#     else:
#         print(40 * '*')
#         print('Wrong input!!!')
#     show_menu()
#
#
# def main():
#     global user_name
#     user_name = getting_name(True)
#     show_menu()
#
#
# user_score = 0
# ai_score = 0
# main()

# #########################################################333
# lower
# upper
# 123
# !@##$%$%^
# len

import string

def main():
    is_lower = input('aya horof koochik dashte bashe? ')
    is_upper = input('aya horof boorg dashte bashe? ')
    is_num = input('aya number dashte bashe? ')
    is_spec = input('aya az sepcial ha estefade shavad? ')
    len_char = input('che tedad bashad? ')
    posible_password = []
    if is_lower in ['yes', 'are', 'ok', '1']:
        posible_password.append(string.ascii_lowercase)
    if is_upper in ['yes', 'are', 'ok', '1']:
        posible_password.append(string.ascii_uppercase)
    if is_num in ['yes', 'are', 'ok', '1']:
        posible_password.append(string.digits)
    if is_spec in ['yes', 'are', 'ok', '1']:
        posible_password.append(string.punctuation)

    make_password(int(len_char), posible_password)


def make_password(tedad, posible_pass):
    password = ''
    for item in range(tedad):
        rand_choice = random.choice(posible_pass)
        password += random.choice(rand_choice)

    print(password)



main()
