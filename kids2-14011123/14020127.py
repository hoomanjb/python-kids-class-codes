# سنگ کاغذ قیچی
# esmeto bgoo
# ejaze nadare alpha
# salam felani khosh amadi
# 1- start
# 2- show score
# 3- edit name
# 4- restart
# 5- exit

# ################################# #
import random

choices = ['1', '2', '3']
ai_score = 0
user_score = 0


def start_game():
    global ai_score
    global user_score
    while True:
        user_choice = input('Enter 1-Sang 2-Kaghaz 3-Gheychi 4-BackToMainMenu: ')
        if user_choice not in ['1', '2', '3', '4']:
            print('Wrong Input!  ')
        else:
            break
    ai_choice = random.choice(choices)
    if user_choice == '1':
        if ai_choice == '1':
            print('Draw....!')
        elif ai_choice == '2':
            print('You Lose...!')
            ai_score += 1
        else:
            print('You Win...!')
            user_score += 1
    elif user_choice == '2':
        if ai_choice == '1':
            print('You Win...!')
            user_score += 1
        elif ai_choice == '2':
            print('Draw....!')
        else:
            print('You Lose...!')
            ai_score += 1
    elif user_choice == '3':
        if ai_choice == '1':
            print('You Lose...!')
            ai_score += 1
        elif ai_choice == '2':
            print('You Win...!')
            user_score += 1
        else:
            print('Draw....!')
    else:
        return


def restart_game():
    global ai_score
    global user_score
    ai_score = 0
    user_score = 0
    print('Restarted Game...!')


def show_score():
    global ai_score
    global user_score
    print(f'Ai Score is: {ai_score}')
    print(f'User Score is: {user_score}')


def get_user_name():
    while True:
        user_name = input('Enter Your name: ')
        if user_name.isalpha():
            print(f'{user_name} Welcome To Sang-Kaghaz-Gheychi Game !')
            break
        else:
            print('Wrong Input! Use Just Alphabet Char')
    return user_name


def show_main_menu():
    print(20 * '#')
    print('Main Menu:')
    print('1- Start Game')
    print('2- Restart Game')
    print('3- Show Score')
    print('4- Edit UserName')
    print('5- Exit')

    return input(': ')


def main():
    user_name = get_user_name()
    while True:
        select = show_main_menu()
        if select == '1':
            start_game()
        elif select == '2':
            restart_game()
        elif select == '3':
            show_score()
        elif select == '4':
            get_user_name()
        elif select == '5':
            print('Exit')
            break
        else:
            print('Wrong Input!')

main()


# Calculator
# addad 1
# addad 2
# 1- jamm
# 2- tafrigh
# ...
# 5- edit adad aval
# 6- edit adad dovom
# 6- exit