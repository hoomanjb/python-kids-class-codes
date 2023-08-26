# import library's we need
import random,time
from colorama import *
fix_for = 0
tie = 0
counter = 0
ai_score = 0
user_score = 0
user_choice = ""
ai_choice_words=["sang","kaghaz","gheychi"]
start_words=["start","play","1","START","PLAY","start ","play ","1 ","START ","PLAY "] # lower()
show_score_words=["2","2 ","showscore","showscore ","show score","show score ","SHOWSCORE","SHOWSCORE "]
restart_game_words=["3","3 ","restartgame","restart game","RESTARTGAME","RESTARTGAME ","restart game ","restartgame "]
edit_name_words=["4 ","4","edit name","EDIT NAME","editname","EDITNANE","editname ","EDITNAME ","edit name "]
quit_words=["exit","quit","5","q","EXIT","QUIT","Q","exit ","exit ","quit ","5 ","q ","EXIT ","QUIT ","Q "]
yes_words=["Yes ","Yes","yes","yes ","y","Y","Y ","y ","YES"]
no_words=["No ","No","no ","no","n","n ","N ","N"]
sang_words=["sang","sang ","1","1 ","SANG","SANG ","s","S","s ","S "]
kaghaz_words=["kaghaz","kaghaz ","2","2 ","KAGHAZ","KAGHAZ","k","k ","K","K "]
gheychi_words=["gheychi","gheychi ","3","3 ","GHEYCHI","GHEYCHI ","g","G","g ","G "]
main_menu_words=["main menu","mainmenu","leave","main menu ","mainmenu ","menu","menu "]
user_name = ""
# write function's
def check_winner(par1,par2):
    if par1 in sang_words:
        par1 = "sang"
    if par1 in kaghaz_words:
        par1 = "kaghaz"
    if par1 in gheychi_words:
        par1 = "gheychi"
    global mosavi,ai_score,user_score,tie
    #ai modes
    if par1 in kaghaz_words and par2 in gheychi_words:
        ai_score += 1
        print(f"your choice is: {par1} and ai choice is : {par2}")
        print(f"{Fore.BLUE}ai{Fore.RESET} won your score is: {user_score} and ai score is: {ai_score}")
    elif par1 in gheychi_words and par2 in sang_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        ai_score += 1
        print(f"ai won your score is: {user_score} and ai score is: {ai_score}")
    elif par1 in sang_words and par2 in kaghaz_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        ai_score += 1
        print(f"ai won your score is: {user_score} and ai score is: {ai_score}")
    #user modes
    elif par1 in kaghaz_words and par2 in sang_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        user_score += 1
        print(f"you won your score is: {user_score} and ai score is: {ai_score}")
    elif par1 in gheychi_words and par2 in kaghaz_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        user_score += 1
        print(f"you won your score is: {user_score} and ai score is: {ai_score}")
    elif par1 in sang_words and par2 in gheychi_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        user_score += 1
        print(f"you won your score is: {user_score} and ai score is: {ai_score}")
    elif par1 in main_menu_words:
        main_menu()
    elif par1 in sang_words and par2 in sang_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        tie += 1
        print(f"tie | tie times: {tie}")
    elif par1 in kaghaz_words and par2 in kaghaz_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        tie += 1
        print(f"tie | tie times: {tie}")
    elif par1 in gheychi_words and par2 in gheychi_words:
        print(f"your choice is: {par1} and ai choice is : {par2}")
        tie += 1
        print(f"tie | tie times: {tie}")
    else:
        print("wrong and score give's to ai :)")
        ai_score += 1
def start():
    print(f"welcome to this game {user_name}")
    while True:
        counter = input("How many times do you want to play? ")
        if counter == "main menu":
            main_menu()
        if counter.isdigit() == False:
            print(Fore.RED + "   please just enter number")
            print(Style.RESET_ALL)
            continue
        elif int(counter) > 60:
            print("you can just play less than 60 times")

        else:
            break
    print(f'ok you should play for {counter} times')
    fix_for = int(counter) + 1
    for i in range(1,fix_for):
        ai_choice = random.choice(ai_choice_words)
        user_choice = input(f"{Fore.BLACK}1/sang {Fore.WHITE}2/kaghaz {Fore.LIGHTBLACK_EX}3/gheychi ? {Style.RESET_ALL}")
        # if user_choice not in three_words:
        #     print(f"{user_choice} not found plesae just enter sang kaghaz ghyechi")
        #     continue
        check_winner(user_choice,ai_choice)
    main_menu()
    # print(f"{ai_score}{}")
def restart_game():
    global mosavi, ai_score, user_score, tie
    ai_score -= ai_score
    user_score -= user_score
    tie -= tie
    print("your score's were reset")
def show_score():
    print(f"ai score is: {ai_score}\nuser score is: {user_score}\nand tie: {tie}")
    time.sleep(5)
def edit_name():
    check_user_name("menu")
def check_user_name(par):
    wrong_number = 1
    global user_name
    while True:
        user_name = input("enter your name please: ")
        if wrong_number == 4:
            print("we are so sorry but we was give warn but you enter your name wrong for 4 times your scores are reset and app close now")
            exit()
        if user_name.isalpha() == False:
            wrong_number += 1
            print(f"please just enter alphabet you have just have {4-wrong_number} choice for enter your name for entering your name")
            continue
        elif len(user_name) > 20:
            print("your name is too long please enter your name shorter than 20 characters")
        else:
            print(f'ok your name changed to {user_name}')
            # user_name = user_name

            break
def main_menu():
    if user_name == "":
        check_user_name("menu")

    while True:
        print(f"{Fore.BLUE}user name is {user_name}")
        print(f"{Fore.GREEN}        1_Start\n{Fore.CYAN}        2_show score\n{Fore.YELLOW}        3_restart game\n{Fore.MAGENTA}        4_edit name\n{Fore.RED}        5_exit{Fore.RESET}")
        read = input("        >")
        if read in start_words:
            start()
            break
        if read in show_score_words:
            show_score()
        if read in restart_game_words:
            restart_game()
        if read in edit_name_words:
            edit_name()
        if read in quit_words:

            break
main_menu()