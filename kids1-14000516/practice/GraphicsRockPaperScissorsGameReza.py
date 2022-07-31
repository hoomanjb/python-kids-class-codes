import random
import tkinter

window = tkinter.Tk()

window.geometry('565x565')

window.title('ROCK PAPER SCISSORS GAME')

user_score = 0
ai_score = 0
user_choice = ''
ai_choice = ''

def show_result():
    global user_score
    global ai_score
    global user_choice
    global ai_choice
    a = 'rock'
    b = 'paper'
    c = 'scissors'
    if user_choice == ai_choice:
        print('Its a draw!')
    elif (user_choice == a and ai_choice == c) or (user_choice == b and ai_choice == a) or (user_choice == c and ai_choice == b):
        print('You won!')
        user_score += 1
    elif (user_choice == c and ai_choice == a) or (user_choice == a and ai_choice == b) or (user_choice == b and ai_choice == c):
        print('The AI won!')
        ai_score += 1

    text_area = tkinter.Text(master=window, height=50, width=50)
    text_area.grid(column=1, row=2)
    result_text = f"""
You chose {user_choice} and the AI chose {ai_choice} , so
your score is {user_score} and the AI's score is {ai_score}"""
    text_area.insert(tkinter.END, result_text)



def rock_clicking():
    global user_choice
    global ai_choice
    user_choice = 'rock'
    ai_choice = random.choice(['rock', 'paper', 'scissors'])
    show_result()

def paper_clicking():
    global user_choice
    global ai_choice
    user_choice = 'paper'
    ai_choice = random.choice(['rock', 'paper', 'scissors'])
    show_result()

def scissors_clicking():
    global user_choice
    global ai_choice
    user_choice = 'scissors'
    ai_choice = random.choice(['rock', 'paper', 'scissors'])
    show_result()


rock_button = tkinter.Button(
    master=window, text='  ROCK  ', bg='skyblue', width=10, command=rock_clicking)
rock_button.grid(column=0, row=1)

paper_button = tkinter.Button(
    master=window, text='  PAPER  ', bg='pink', width=10, command=paper_clicking)
paper_button.grid(column=1, row=1)

scissor_button = tkinter.Button(
    master=window, text='  SCISSORS  ', bg='lightgreen', width=10, command=scissors_clicking)
scissor_button.grid(column=2, row=1)
window.mainloop()


