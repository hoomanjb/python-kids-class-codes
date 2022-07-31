import random
user_score=0
ai_score=0

def getting_name():
    user_name=input('please enter your name.')
    return user_name

def select_menu(user_name):
    text = input(f'Hello {user_name},please select what do you want to do,by selecting from these options: 1)start  2)score  3)exit')
    user_choice = input(text)
    return user_choice

def user_exit():
    print(f'see you soon!:{user_score} and {ai_score}')

def show_score():
    print(f'your score is:{user_score}  ai score is:{ai_score}')

def getting_user_choice(user_name):
    text2 = input(f"{user_name}please select your choice: 1)rock  2)paper  3)scissors")
    user_choice = input(text2)
    return user_choice

def checking_answer(user_choice,ai_choice):
    global user_score
    global ai_score
    if user_choice == ai_choice:
        print('Equal!')
        user_score += 1
        ai_score += 1
    elif user_choice == 'rock' and ai_choice == 'paper':
        print('you lost!')
        ai_score += 1
    elif user_choice == "rock" and ai_choice == 'scissors':
        print('you win!')
        user_score += 1
    elif user_choice == 'paper' and ai_choice == 'rock':
        print('you win!')
        user_score += 1
    elif user_choice == "paper" and ai_choice == 'scissors':
        print('you lost!')
        ai_score += 1
    elif user_choice == 'scissors' and ai_choice == 'rock':
        print('you lost!')
        ai_score += 1
    elif user_choice == "scissors" and ai_choice == "paper":
        print('you win!')
        user_score += 1
def main():
    user_name=getting_name()
    select_menu=(user_name)
    if select_menu == 'exit' or select_menu == "3":
        user_exit()
    elif select_menu == 'score' or select_menu == '2':
        show_score()
    elif select_menu == 'start' or select_menu == "1":

        user_choice = getting_user_choice(user_name)
        the_odds = ['rock',"paper",'scissors']
        ai_choice = random.choice(the_odds)
        checking_answer(user_choice, ai_choice)
        print(f'your score:{user_score} ai score:{ai_score}')









