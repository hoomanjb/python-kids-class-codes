import random

user_score = 0
ai_score = 0


def getting_name():
    user_name = input('enter your name: ')
    return user_name


def getting_selected_menu(user_name):
    text = f'mr/miss {user_name} plz select from these numbers: 1)start 2)emtiazat 3)change-name 4)exit'
    user_choice = input(text)
    return user_choice


def exiting(user_name):
    print(f' mr/miss {user_name} khosh oomadi emtiaze shoma {user_score} va emtiaze ai {ai_score}')


def show_scores(user_name):
    print(f' mr/miss {user_name} emtiaze shoma {user_score} va emtiaze ai {ai_score}')


def getting_user_choice(user_name):
    while 1:
        text = f'mr/miss {user_name} plz select from these options: 1)sang 2)kaghaz 3)gheychi'
        user_choice = input(text)
        if user_choice == 'sang' or user_choice == 'kaghaz' or user_choice == 'gheychi':
            return user_choice
        else:
            print("I didn't understand")
            continue


def check_winner(user_choice, ai_choice):
    global user_score
    global ai_score
    a = 'sang'
    b = 'kaghaz'
    c = 'gheychi'
    if user_choice == ai_choice:
        print(' mosavi shod be naafe davar')
        user_score += 1
        ai_score += 1
    elif (user_choice == a and ai_choice == c) or (user_choice == b and ai_choice == a) or (user_choice == c and ai_choice == b):
        print('bordi afarin')
        user_score += 1
    elif (user_choice == c and ai_choice == a) or (user_choice == a and ai_choice == b) or (user_choice == b and ai_choice == c):
        print('ai bord')
        ai_score += 1


def restart_game(user_name):
    text = (f'mr/miss {user_name},please select one option: 1)play again 2)go to menu')
    user_pick = input(text)
    return user_pick


def shorooe_bazi(user_name):
    global user_score
    global ai_score
    user_choice = getting_user_choice(user_name)
    ehtemalat = ['sang', 'kaghaz', 'gheychi']
    ai_choice = random.choice(ehtemalat)
    print(user_choice)
    print(ai_choice)
    check_winner(user_choice, ai_choice)
    print(f'dar hale hazer emtiaze shoma {user_score} va emtiaze ai {ai_score}')


def main():
    user_name = getting_name()
    while 1:
        user_selected_menu = getting_selected_menu(user_name)
        if user_selected_menu == 'exit' or user_selected_menu == '4':
            exiting(user_name)
            break
        elif user_selected_menu == 'change-name' or user_selected_menu == '3':
            user_name = getting_name()
        elif user_selected_menu == 'emtiazat' or user_selected_menu == '2':
            show_scores(user_name)
        elif user_selected_menu == 'start' or user_selected_menu == '1':
            while 1:
                shorooe_bazi(user_name)
                user_pick = restart_game(user_name)
                if user_pick == 'go to menu' or user_pick == '2':
                    break
                elif user_pick == 'play again' or user_pick == '1':
                    continue
                else:
                    print("I didn't understand")
        else:
            print("I didn't understand")


main()
