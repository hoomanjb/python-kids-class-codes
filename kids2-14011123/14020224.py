# python starter -> 3ta dore (html-css, Database, Git, Front, Security, Deploy, Network, Design)
# python advanced -> advanced ()
# Multithread - Async - MultiProcess
# bot-telegram
# Design Pattern - Algo - Struct
# sorting
# MVC - MVT -
# Django starter
# Django Advanced
# back end - app va web -> Django - FastAPI - Flask - Pyramid
# front -> js -> React - Angular - nextjs
# DB -> postgresql - mysql - mssql - mongodb
#
#
# #################################### #
# mashin hesab

import tkinter as tk
import random

# window = tk.Tk()
# window.geometry('500x500')
# window.title('SANG KAGHAZ GHEYCHI GAME')
#
# user_score = 0
# ai_score = 0
# user_choice = ''
# ai_choice = ''
# result = ''
#
#
# def random_ai_choice():
#     return random.choice(['sang', 'kaghaz', 'gheychi'])
#
#
# def who_is_winner():
#     global user_choice
#     global ai_choice
#     # result -> 0 = equal , 1 = ai , 2 = user
#     if user_choice == ai_choice:
#         return 0
#     elif user_choice == 'sang':
#         if ai_choice == 'kaghaz':
#             return 1  # ai is winner
#         else:
#             return 2  # user is winner
#     elif user_choice == 'kaghaz':
#         if ai_choice == 'sang':
#             return 2  # user is winner
#         else:
#             return 1  # ai is winner
#     elif user_choice == 'gheychi':
#         if ai_choice == 'kaghaz':
#             return 2  # user is winner
#         else:
#             return 1  # ai is winner
#
#
# def check_result():
#     global user_choice
#     global ai_choice
#     global user_score
#     global ai_score
#     global result
#     winner = who_is_winner()
#     if winner == 0:
#         result = 'MOSAVIIIIII'
#     elif winner == 1:
#         result = 'AI IS WINNERRRR'
#         ai_score += 1
#     else:
#         result = 'USER IS WINNERRR'
#         user_score += 1
#
#     message = f"""
#     {result}
#
#     user choice : {user_choice}
#     ai choice : {ai_choice}
#
#     user score : {user_score}
#     ai score : {ai_score}
#     """
#     text_box.delete('1.0', 'end')
#     text_box.insert('0.0', message)
#
#
# def restart_game():
#     global user_score
#     global ai_score
#     user_score = 0
#     ai_score = 0
#
#
# def press_sang():
#     global user_choice
#     global ai_choice
#     user_choice = 'sang'
#     ai_choice = random_ai_choice()
#     check_result()
#
#
# def press_kaghaz():
#     global user_choice
#     global ai_choice
#     user_choice = 'kaghaz'
#     ai_choice = random_ai_choice()
#     check_result()
#
#
# def press_gheychi():
#     global user_choice
#     global ai_choice
#     user_choice = 'gheychi'
#     ai_choice = random_ai_choice()
#     check_result()
#
#
# sang_button = tk.Button(text='Sang', bg='skyblue', width=10, command=press_sang)
# sang_button.grid(row=1, column=0)
#
# kaghaz_button = tk.Button(text='Kaghaz', bg='pink', width=10, command=press_kaghaz)
# kaghaz_button.grid(row=1, column=1)
#
# gheychi_button = tk.Button(text='Gheychi', bg='lightgreen', width=10, command=press_gheychi)
# gheychi_button.grid(row=1, column=2)
#
# text_box = tk.Text(master=window, height=15, width=30, bg='gray', font='arial')
# text_box.grid(row=2, column=1)
#
# reset_button = tk.Button(text='Reset', bg='red', width=10, command=restart_game)
# reset_button.grid(row=3, column=1)
#
# window.mainloop()


# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()

# Set geometry
root.geometry("300x300")

# Set title
root.title("Rock Paper Scissor Game")

# Computer Value
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}


# Reset The Game


def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")
    l4.config(text="")


# Disable the Button


def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"


# If player selected rock


def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=c_v)
    button_disable()


# If player selected paper


def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=c_v)
    button_disable()


# If player selected scissor


def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Tasavi"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=c_v)
    button_disable()


# Add Labels, Frames and Button
Label(root,
      text="Rock Paper Scissor",
      font="normal 20 bold",
      fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
           text="Player              ",
           font=10)

l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold")

l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="white",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock",
            font=10, width=7,
            command=isrock)

b2 = Button(frame1, text="Paper ",
            font=10, width=7,
            command=ispaper)

b3 = Button(frame1, text="Scissor",
            font=10, width=7,
            command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Reset Game",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)

# Execute Tkinter
root.mainloop()