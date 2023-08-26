import random
def user_name_checker():
    while True:
        user_name = input("*********** enter your user name:")
        if user_name.isalpha():
            return user_name
        else:
            print("user_name must be ONLY letters")

def user_choices_checker():
    choices = ["sang", "kaghaz", "gheichi"]
    while True:
        print("enter 1 to go to main menu")
        user_choice = input("******* sang or kaghaz or gheichi:")
        if user_choice == "1":
            main_menu()
            break
        elif user_choice in choices:
            return user_choice
        else:
            print("please choose between sang, kaghaz, gheichi")

def main_game(user_choice):
    # ai wins = 1
    # user wins =  2
    # tie = 0
    global name
    choices = ["sang", "kaghaz", "gheichi"]
    computer_choice = random.choice(choices)
    if computer_choice == user_choice:
        print("mosavi!!!!!!")
        return 0
    elif user_choice == "sang":
        if computer_choice == "kaghaz":
            print("computer wins!!!")
            return 1
        else:
            print(f"{name} win!!!!!!!")
            return 2
    elif user_choice == "gheichi":
        if computer_choice == "sang":
            print("computer wins!!!!")
            return 1
        else:
            print(f"{name} wins!!!!")
            return 2
    else:
        if computer_choice == "gheichi":
            print("computer wins!!!!")
            return 1
        else:
            print(f"{name} wins!!!!")
            return 2

def points_checker(user_score, computer_score, ties):
    point = main_game(user_choices_checker())
    input("press enter to go to the main menu:")
    print("**************")
    if point == 0:
        ties += 1
    elif point == 1:
        computer_score += 1
    elif point == 2:
        user_score += 1
    return user_score, computer_score, ties

def points_shower(user_score,computer_score,mosavi):
    plays = user_score + computer_score + mosavi
    print(f"user score is: {user_score},computer score is: {computer_score},ties : {mosavi}, how many times played: {plays}")
    input("press enter to go to main menu:")
    print("*******************")

name = user_name_checker()
user_point, computer_point, tie_point = 0, 0, 0
def main_menu():
    global user_point
    global computer_point
    global tie_point
    global name
    options = ["1", "2", "3", "4", "5"]
    print("*********** main menu ***********")
    print(f"user name:{name}")
    while True:
        print("1.start game")
        print("2.restart game")
        print("3.show points")
        print("4.change name")
        print("5.exit game")
        chosen = input("what do you want?")
        print("***************")
        if chosen in options:
            main_menu_uption = chosen
            if main_menu_uption == "1":
                user_point, computer_point, tie_point = points_checker(user_point, computer_point, tie_point)
            elif main_menu_uption == "2":
                user_point, computer_point, tie_point = 0, 0, 0
                print("restarted")
                print("*****************")
            elif main_menu_uption == "3":
                points_shower(user_point, computer_point, tie_point)
            elif main_menu_uption == "4":
                name = user_name_checker()
            else:
                print("thanks for playing")
                return 1
            break
        else:
            print("please choose one of the above")
            print("*****************************")
def game_opener():
    while True:
        end_detector = main_menu()
        if end_detector == 1:
            break
        else:
            continue

game_opener()