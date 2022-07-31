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
    text = f'mr/miss {user_name} plz select from these numbers: 1)sang 2)kaghaz 3)gheychi'
    user_choice = input(text)
    return user_choice


def check_winner(user_choice, ai_choice):
    global user_score
    global ai_score
    if user_choice == ai_choice:
        print(' mosavi shod b naafe davar')
        user_score += 1
        ai_score += 1
    elif user_choice == 'sang' and ai_choice == 'gheychi':
        print('afarin pirooz shodi')
        user_score += 1


def main():
    user_name = getting_name()
    user_selected_menu = getting_selected_menu(user_name)
    if user_selected_menu == 'exit' or user_selected_menu == '4':
        exiting(user_name)
    elif user_selected_menu == 'change-name' or user_selected_menu == '3':
        user_name = getting_name()
    elif user_selected_menu == 'emtiazat' or user_selected_menu == '2':
        show_scores(user_name)
    elif user_selected_menu == 'start' or user_selected_menu == '1':
        user_choice = getting_user_choice(user_name)
        ehtemalat = ['sang', 'kaghaz', 'gheychi']
        ai_choice = random.choice(ehtemalat)
        check_winner(user_choice, ai_choice)
        print(f'dar hale hazer emtiaze shoma {user_score} va emtiaze ai {ai_score}')
        # ??? again 


main()
