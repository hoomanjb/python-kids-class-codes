# # sang kaghaz gheychi
# # Start Game
# # esmeto begoo:
# # hatman horofe alefba bayad bezanam
# #
# # ######### Main Menu ##########
# # UserName: hooman    ##########
# # 1- start game
# # 2- show score
# # 3- restart game
# # 4- edit name
# # 5- exit
# # ############################
#
# # 1-
# # ##############
# # 1-sang 2-kaghaz 3-gheychi 4-back-to-main-menu
# # barande shodi
# # 1- edame bedi 2-back-to-main-menu
#
#
# # ##############
# # user = 0 - ai= 0
# # ##############
#
#
# # restart-game -> score 0
# import colorama
# from colorama import Fore, Back, Style
# import random
#
# ######################################################################
#
#
# # Sang_Kaqaz_Qeichi
# sets_win = 0
# ai_score = 0
# user_score = 0
#
#
# def who_is_winner(user, ai):
#     # 0 = mosavi , 1 = user , ai = 2
#     if user == 'sang':
#         if ai == 'kaqaz':
#             return 2
#         elif ai == 'qeichi':
#             return 1
#     elif user == 'kaqaz':
#         if ai == 'sang':
#             return 1
#         elif ai == 'qeichi':
#             return 2
#     else:
#         if ai == 'sang':
#             return 2
#         elif ai == 'kaqaz':
#             return 1
#     return 0
#
#
# def score_calculate(score):
#     global ai_score
#     global user_score
#     if score == 2:
#         print(Fore.YELLOW + 'AI is winner...' + Fore.RESET)
#         ai_score += 1
#     elif score == 1:
#         print(Fore.GREEN + 'You are winner...' + Fore.RESET)
#         user_score += 1
#     else:
#         print(Fore.BLUE + "it's tie." + Fore.RESET)
#     return ai_score, user_score
#
#
# def check_user_input():
#     while True:
#         user_input = input('sang , kaqaz , qeichi ? ')
#         if user_input in ['sang', 'kaqaz', 'qeichi']:
#             return user_input
#         else:
#             print(Fore.RED + 'Wrong!Try again...' + Fore.RESET)
#
#
# def game():
#     global sets_win
#     global ai_score
#     global user_score
#     for i in range(5):
#         user_choice = check_user_input()
#         ai_choice = random.choice(['sang', 'kaqaz', 'qeichi'])
#         print('My choice is ' + Style.BRIGHT + f'{ai_choice}' + Style.RESET_ALL)
#         result = who_is_winner(user_choice, ai_choice)
#         ai_score, user_score = score_calculate(result)
#         print(f'AI score is ' + Fore.YELLOW + f'{ai_score}' + Fore.RESET)
#         print(f'Your score is ' + Fore.GREEN + f'{user_score}' + Fore.RESET)
#         print('-' * 50)
#     mosavi = 5 - (user_score + ai_score)
#     text = 'your score is : ' + Fore.GREEN + f'{user_score}' + Fore.RESET + ' and AI score is : ' + Fore.YELLOW + f'{ai_score}' + Fore.RESET + ' and the ties is : ' + Fore.BLUE + f'{mosavi}' + Fore.RESET
#     print(text)
#     if user_score > ai_score:
#         sets_win += 1
#         print('You ' + Fore.GREEN + 'WIN'' this Game!' + Fore.RESET)
#     elif user_score < ai_score:
#         print("I'm a " + Fore.GREEN + 'Winner' + Fore.RESET + ".hahahaha")
#     else:
#         print(Fore.GREEN + 'Good Game,We are Tie.' + Fore.RESET)
#
#     return sets_win
#
#
# ########################################################
#
#
# name = input('Enter your Name: ')
#
#
# def name_q():
#     global name
#     while True:
#         if name.isalpha():
#             name = name.capitalize()
#             print(
#                 f'Hello, Welcome to the game ' + Style.BRIGHT + f'{name}' + Style.RESET_ALL + '. I hope you enjoy the Game:)')
#             break
#         else:
#             print(Fore.RED + 'Wrong Input! Please enter the alphabet' + Fore.RESET)
#             name = input('Enter your Name: ')
#     return name
#
#
# def main_menu():
#     global name_q
#     global name
#
#     print('')
#     print(Style.BRIGHT + 8 * '#' + ' MAIN MENU ' + Style.RESET_ALL + 8 * '#')
#     print('')
#
#     print(Fore.RED + Style.BRIGHT + 'User_Name: ' + Fore.RESET + f'{name}' + Style.RESET_ALL + Fore.RESET)
#
#     print(Fore.RED + 3 * '#' + ' 1-' + Style.BRIGHT + '  Start ' + Style.RESET_ALL)
#
#     print(Fore.RED + 3 * '#' + ' 2 - ' + Style.BRIGHT + 'Show Score ' + Style.RESET_ALL)
#
#     print(Fore.RED + 3 * '#' + ' 3 - ' + Style.BRIGHT + 'Restart ' + Style.RESET_ALL)
#
#     print(Fore.RED + 3 * '#' + ' 4 - ' + Style.BRIGHT + 'Edit Name ' + Style.RESET_ALL)
#
#     print(Fore.RED + 3 * '#' + ' 5 - ' + Style.BRIGHT + 'Exit ' + Fore.RESET + Style.RESET_ALL)
#
#     while True:
#         choice = input('enter your choice: ')
#         print('')
#         if choice in ['1', '2', '3', '4', '5']:
#             return choice
#             break
#         else:
#             print('Wrong Input!Try again...')
#             continue
#
#
# def opp(choice):
#     global sets_win
#     global ai_score
#     global user_score
#     global name
#     round = 1
#     while True:
#         if choice == '1':
#             print(Fore.RED + '#' * 8 + f' Lets Go! Round {round} ' + '#' * 8 + Fore.RESET)
#             game()
#             round += 1
#             ai_score = 0
#             user_score = 0
#             break
#         elif choice == '2':
#             print(Style.BRIGHT + f'The sets you won is : ' + Fore.GREEN + f'{sets_win}' + Fore.RESET)
#             break
#         elif choice == '3':
#             round == 0
#             sets_win == 0
#             break
#         elif choice == '4':
#             name = input('Enter your New Name: ')  # inja app bug dare
#             print(
#                 Fore.GREEN + f"Your name has been successfully changed!Now you are " + Style.BRIGHT + f"'{name.capitalize()}'" + Fore.RESET + Style.RESET_ALL)
#             break
#         elif choice == '5':
#             break
#         else:
#             print('Wrong Input.Try again.')
#
#
# name_q()
# while True:
#     user_choice = main_menu()
#     opp(user_choice)
#     if user_choice == '5':
#         break
#     else:
#         continue

# import sys
# from termcolor import colored, cprint
#
# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)

# from termcolor import colored
#
# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
#
# print(text)


# from colorama import Fore, Back, Style
#
# print(Fore.RED + 'some red text')


