# bazi sang kaghaz gheychi
# 10 dast bazi konid
# karbar ye ai
# chek konid ki barande shode
# harki brande shode bood 1 emtiaz begire
# baade 10 dast natije koli ro begi
# user 4 va ai 4 va 2 mosavi
import random


# def mini_game(emtiaz, ai_emtiaz, ai, tie):
#     while True:
#         user_input = input("sang, kaqhaz, qheichi:")
#         if user_input in ["sang", "kaqhaz", "qheichi"]:
#             if ai == "sang" and user_input == "kaqhaz":
#                 print("good job")
#                 emtiaz += 1
#             elif ai == "sang" and user_input == "sang":
#                 tie += 1
#             elif ai == "sang" and user_input == "qheichi":
#                 print("you lost!")
#                 ai_emtiaz += 1
#             elif ai == "kaqhaz" and user_input == "kaqhaz":
#                 tie += 1
#             elif ai == "kaqhaz" and user_input == "sang":
#                 print("you lost!")
#                 ai_emtiaz += 1
#             elif ai == "kaqhaz" and user_input == "qheichi":
#                 print("good job")
#                 emtiaz += 1
#             elif ai == "qheichi" and user_input == "kaqhaz":
#                 print("you lost!")
#                 ai_emtiaz += 1
#             elif ai == "qheichi" and user_input == "qheichi":
#                 tie += 1
#             elif ai == "qheichi" and user_input == "sang":
#                 print("good job")
#                 emtiaz += 1
#                 break
#         else:
#             print("wrong option!!!")
#     return emtiaz and ai_emtiaz and tie
#
# score, ai_score, mosavi = 0, 0, 0
#
# for item in range(10):
#     ai_choice = random.choice(["sang", "kaqhaz", "qheichi"])
#     score, ai_score, mosavi = mini_game(score, ai_score, ai_choice, mosavi)
#
# text = f"your score {score} ai score {ai_score} ties {mosavi}"
# print(text)


# bazi sang kaghaz gheychi
# 10 dast bazi konid  -> loop
# karbar ye ai  -> input, random
# chek konid ki barande shode -> function, validation
# harki brande shode bood 1 emtiaz begire
# baade 10 dast natije koli ro begi
# user 4 va ai 4 va 2 mosavi

def who_is_winner(user, ai):
    # return -> 0 == Davar , 1 == User , 2 == Ai
    if user == 'Sang':
        if ai == 'Kaghaz':
            return 2
        elif ai == 'Gheychi':
            return 1
    elif user == 'Kaghaz':
        if ai == 'Sang':
            return 1
        elif ai == 'Gheychi':
            return 2
    else:
        if ai == 'Sang':
            return 2
        elif ai == 'Kaghaz':
            return 1
    return 0


def score_calculate(score):
    global user_score
    global ai_score
    if score == 2:
        print('Ai Is Winner...')
        ai_score += 1
    elif score == 1:
        print('User is Winner...')
        user_score += 1
    else:
        print('Tie....')
    return user_score, ai_score


def check_user_input():
    while True:
        a = 10
        user_input = input('enter Sang or Kaghaz or Gheychi: ')
        if user_input in ['Sang', 'Kaghaz', 'Gheychi']:
            return user_input
        else:
            print('Wrong Input...!')


def mini_game():
    global user_score
    global ai_score
    for item in range(10):
        user_choice = check_user_input()
        ai_choice = random.choice(['Sang', 'Kaghaz', 'Gheychi'])
        result = who_is_winner(user_choice, ai_choice)
        user_score, ai_score = score_calculate(result)
        print(f'user score is: {user_score}')
        print(f'ai score is: {ai_score}')
        print('#' * 50)

user_score, ai_score = 0, 0
mini_game()
mosavi = 10 - (user_score + ai_score)
text = f"your score {user_score} ai score {ai_score} ties: {mosavi}"
print(text)
