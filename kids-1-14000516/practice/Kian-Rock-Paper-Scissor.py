import tkinter
import random

font_tuple = ('Comic Sans MS', 10, 'bold')
window = tkinter.Tk()

window.geometry('600x600')

window.title('ROCK PAPER SCISSOR GAME')

user_score = 0
ai_score = 0
user_choice = ''
ai_choice = ''
RPS = ['rock', 'paper', 'scissor']


def show_result():
    global user_score
    global ai_score
    global user_choice
    global ai_choice
    a = 'rock'
    b = 'paper'
    c = 'scissor'
    if user_choice == ai_choice:
        print(' mosavi shod be naafe davar')
    elif (user_choice == a and ai_choice == c) or (user_choice == b and ai_choice == a) or (user_choice == c and ai_choice == b):
        print('bordi afarin')
        user_score += 1
    elif (user_choice == c and ai_choice == a) or (user_choice == a and ai_choice == b) or (user_choice == b and ai_choice == c):
        print('ai bord')
        ai_score += 1
    text_area = tkinter.Text(master=window, height=20, width=50, bg='lightgreen', font=font_tuple, fg='blue')
    text_area.grid(column=1, row=2)
    result_text = f"""
shoma {user_choice} entekhab kardin va ai {ai_choice} pas
emtiaze shoma {user_score} va emtiaze ai mishe {ai_score}"""
    text_area.insert(tkinter.END, result_text)


def rock_cliking():
    global user_choice
    global ai_choice
    user_choice = 'rock'
    ai_choice = random.choice(RPS)
    show_result()


def paper_click():
    global user_choice
    global ai_choice
    user_choice = 'paper'
    ai_choice = random.choice(RPS)
    show_result()

def scissor_click():
    global user_choice
    global ai_choice
    user_choice = 'scissor'
    ai_choice = random.choice(RPS)
    show_result()

rock_button = tkinter.Button(
    master=window, text='  ROCK  ', bg='skyblue', width=10, command=rock_cliking, fg='gray')
rock_button.grid(column=0, row=1)

paper_button = tkinter.Button(
    master=window, text='  PAPER  ', bg='pink', width=10, command=paper_click, fg='white')
paper_button.grid(column=1, row=1)

scissor_button = tkinter.Button(
    master=window, text='  SCISSOR  ', bg='black', width=10, command=scissor_click, fg='silver')
scissor_button.grid(column=2, row=1)
window.mainloop()