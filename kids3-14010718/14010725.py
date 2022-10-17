# lambda

# user -> name-boy   -- name-girl

# def test(b): return b + 10
#
#
#
# a = lambda name: name + '-boy'
# c = a('akbar')
# print(a('20'))
# print(c)
# print(test(20))
#
# a = print()
# b = print
#
# print(a)
# print(b)
# b('salam chetori')

# x = lambda a, b: a * b
# print(x(5, 10))

# def test(a):
#     return lambda b: a * b
#
# x = test(3)
# y = test(5)
# z = test(7)
# n = test(10)
#
# print(x(5))
# print(x(9))
# q = lambda e: e + 10
# j = q(2)
# h = q(5)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('DOOOOOOOOOOOZ GAME')

button1 = ttk.Button(root, text=' ')
button1.grid(row=0, column=0, ipadx=70, ipady=70)
button1.config(command=lambda: button_click(1))

button2 = ttk.Button(root, text=' ')
button2.grid(row=0, column=1, ipadx=70, ipady=70)
button2.config(command=lambda: button_click(2))

button3 = ttk.Button(root, text=' ')
button3.grid(row=0, column=2, ipadx=70, ipady=70)
button3.config(command=lambda: button_click(3))

button4 = ttk.Button(root, text=' ')
button4.grid(row=1, column=0, ipadx=70, ipady=70)
button4.config(command=lambda: button_click(4))

button5 = ttk.Button(root, text=' ')
button5.grid(row=1, column=1, ipadx=70, ipady=70)
button5.config(command=lambda: button_click(5))


button6 = ttk.Button(root, text=' ')
button6.grid(row=1, column=2, ipadx=70, ipady=70)
button6.config(command=lambda: button_click(6))


button7 = ttk.Button(root, text=' ')
button7.grid(row=2, column=0, ipadx=70, ipady=70)
button7.config(command=lambda: button_click(7))


button8 = ttk.Button(root, text=' ')
button8.grid(row=2, column=1, ipadx=70, ipady=70)
button8.config(command=lambda: button_click(8))


button9 = ttk.Button(root, text=' ')
button9.grid(row=2, column=2, ipadx=70, ipady=70)
button9.config(command=lambda: button_click(9))


player_turn = tk.Label(root, text='P1 turn!')
player_turn.grid(row=3, column=0, ipadx=70, ipady=70)

reset_button = tk.Button(root, text='RESTART', bg='skyblue', command=lambda: restart_game())
reset_button.grid(row=3, column=1, ipadx=30, ipady=30)

game_help = tk.Label(root, text='P1 is X \n\n P2 is O')
game_help.grid(row=3, column=2, ipadx=70, ipady=70)

a = 1
b = 0
c = 0

def restart_game():
    global a, b, c
    a = 1
    b = 0
    c = 0
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    button1.state(['!disabled'])
    button2.state(['!disabled'])
    button3.state(['!disabled'])
    button4.state(['!disabled'])
    button5.state(['!disabled'])
    button6.state(['!disabled'])
    button7.state(['!disabled'])
    button8.state(['!disabled'])
    button9.state(['!disabled'])


def disable_click():
    button1.state(['disabled'])
    button2.state(['disabled'])
    button3.state(['disabled'])
    button4.state(['disabled'])
    button5.state(['disabled'])
    button6.state(['disabled'])
    button7.state(['disabled'])
    button8.state(['disabled'])
    button9.state(['disabled'])


def button_click(box_id):
    global a, b, c
    # player1
    if box_id == 1 and button1['text'] == ' ' and a == 1:
        button1['text'] = 'X'
        a = 0
        b += 1
    if box_id == 2 and button2['text'] == ' ' and a == 1:
        button2['text'] = 'X'
        a = 0
        b += 1
    if box_id == 3 and button3['text'] == ' ' and a == 1:
        button3['text'] = 'X'
        a = 0
        b += 1
    if box_id == 4 and button4['text'] == ' ' and a == 1:
        button4['text'] = 'X'
        a = 0
        b += 1
    if box_id == 5 and button5['text'] == ' ' and a == 1:
        button5['text'] = 'X'
        a = 0
        b += 1
    if box_id == 6 and button6['text'] == ' ' and a == 1:
        button6['text'] = 'X'
        a = 0
        b += 1
    if box_id == 7 and button7['text'] == ' ' and a == 1:
        button7['text'] = 'X'
        a = 0
        b += 1
    if box_id == 8 and button8['text'] == ' ' and a == 1:
        button8['text'] = 'X'
        a = 0
        b += 1
    if box_id == 9 and button9['text'] == ' ' and a == 1:
        button9['text'] = 'X'
        a = 0
        b += 1

    # player 2
    if box_id == 1 and button1['text'] == ' ' and a == 0:
        button1['text'] = 'O'
        a = 1
        b += 1
    if box_id == 2 and button2['text'] == ' ' and a == 0:
        button2['text'] = 'O'
        a = 1
        b += 1
    if box_id == 3 and button3['text'] == ' ' and a == 0:
        button3['text'] = 'O'
        a = 1
        b += 1
    if box_id == 4 and button4['text'] == ' ' and a == 0:
        button4['text'] = 'O'
        a = 1
        b += 1
    if box_id == 5 and button5['text'] == ' ' and a == 0:
        button5['text'] = 'O'
        a = 1
        b += 1
    if box_id == 6 and button6['text'] == ' ' and a == 0:
        button6['text'] = 'O'
        a = 1
        b += 1
    if box_id == 7 and button7['text'] == ' ' and a == 0:
        button7['text'] = 'O'
        a = 1
        b += 1
    if box_id == 8 and button8['text'] == ' ' and a == 0:
        button8['text'] = 'O'
        a = 1
        b += 1
    if box_id == 9 and button9['text'] == ' ' and a == 0:
        button9['text'] = 'O'
        a = 1
        b += 1


root.mainloop()

