# import random
# def player_name_cheking_part():
#     while True:
#         player_name = input('enter your username: ')
#         if player_name.isdigit():
#             print('your username should not have and digit charachters.')
#         else:
#           return player_name
#
# def user_choice_cheking_part():
#     the_player_chocies = ['sang', 'kaghaz', 'gheichi']
#     while True:
#         print('please enter number 00 if you wana go to the main menu')
#         players_choice = input('sang or khagaz or gheichi: ')
#         if players_choice == '00':
#             MAIN_MENU()
#             break
#         elif players_choice in the_player_chocies:
#             return players_choice
#         else:
#             print('Your choices are only and only sang, kaghaz and gheichi. Please choose from these options not somthing else')
#
#
# def the_game(choice):
#     chocies = ['sang', 'kaghaz', 'gheichi']
#     computer_choice = random.choice(chocies)
#     computer_score = 0
#     player_score = 0
#     while True:
#         if choice == computer_choice:
#             print("The game equalised")
#         elif player == "Rock":
#             if computer == "Paper":
#                 print("You lose!")
#                 computer_score += 1
#             else:
#                 print("You win!")
#                 player_score += 1
#         elif player == "Paper":
#             if computer == "Scissors":
#                 print("You lose!")
#                 ai_score += 1
#             else:
#                 print("You win!")
#                 user_score += 1
#         elif user == "Scissors":
#             if computer == "Rock":
#                 print("You lose!")
#                 computer_score += 1
#             else:
#                 print("You win!")
#                player_score += 1
#         elif player == 'End':
#             print("The Final Scores:")
#             print(f"computer:{computer_score}")
#             print(f"player:{player_score}")
#             break