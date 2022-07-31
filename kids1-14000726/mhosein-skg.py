import random

computer_score = 0
user_score = 0
def getting_user_name():# tabe name
    while True:
        name = input(' enter your name : ')
        if name.isalpha():
            return name
        else:
            print('IS WRONGGGG!!!!!! TRY AGAIN')

user_name = getting_user_name()
while True: #halghe menu
##########################################################
    print()
    print('Hello, welcome to Sang Kaghaz Gheychi Game *', user_name,'*')
    print()
    print('MAIN MENU')
    print('CHOOSE FROM MENU:')
    print('1- Start GAME: ')
    print('2- Show Score: ')
    print('3- Edit Name: ')
    print('4- Exit')
##########################################################
    selected_menu = input()
    if selected_menu == '4':
        print('By By')
        break
    if selected_menu == '3':
        user_name = getting_user_name()
        continue
    if selected_menu == '2':
        print(f'{user_name} score is {user_score} and computer score is {computer_score}')
        print( )
        continue
    if selected_menu == "1":
        print("start game ")
        # computer_score = 0
        # user_score = 0
        while True:
            def check_win(user, computer):#tabe chek kardan barande shodan user
                if (user == 's' and computer == 'gheychi') or (user == 'g' and computer == 'kaghaz') or (user == 'k' and computer == 'sang'):
                   return True
            print()
            user_choice = input(f"*{user_name}* entekhab kon 's' baray sang ya 'k' baray kaghaz ya 'g' baray gheychi *** va M baraye menu: ")
            choices_com = ["kaghaz", "gheychi", "sang"]
            random_choice = random.choice(choices_com)
            if user_choice == 'm' or user_choice == 'M':
                break
            if user_choice == random_choice:
                print( )
                print(f"{user_name} ba computer mosavi shodid! chon entekhab computer is {random_choice}")
            if check_win(user_choice, random_choice):
                user_score +=1
                print( )
                print(f"wow! {user_name} bordi! chon entekhab computer {random_choice} bood***"
                      f" emtiyaz {user_name}   {user_score} va emtiyaz computer {computer_score}")
            if check_win(user_choice, random_choice) != True:
                computer_score +=1
                print( )
                print(f"oh! {user_name} bakhti! chon entekhab computer {random_choice} bood***"
                      f" emtiyaz {user_name}  {user_score} va emtiyaz computer {computer_score}")
