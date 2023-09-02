from tkinter import *

root = Tk()
root.title('shiba calculator')
root.geometry('280x370')

def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(END, str(current) + str(number))

def clear_display():
    display.delete(0, END)

def calculate():
    expression = display.get()
    expression = expression.replace('x', '*')
    expression = expression.replace('/', '/')
    answer = eval(expression)
    display.delete(0, END)
    display.insert(END, answer)

buttons = [
    ['1', 0, 60], ['2', 70, 60], ['3', 140, 60], ['4', 210, 60],
    ['5', 0, 130], ['6', 70, 130], ['7', 140, 130], ['8', 210, 130],
    ['9', 0, 200], ['0', 70, 200]
]

for button in buttons:
    bt = Button(root, text=button[0], fg='white', bg='dark green', font=('Arial', 15), width=5, height=2, bd=5, relief=GROOVE, command=lambda button=button[0]: button_click(button))
    bt.place(x=button[1], y=button[2])

bt_answer = Button(root, text='Answer', fg='white', bg='navy blue', font=('Arial', 15), width=11, height=2, bd=5, relief=GROOVE, command=calculate)
bt_answer.place(x=140, y=200)

operators = ['+', '-', 'x', '/']
for i, operator in enumerate(operators):
    bt = Button(root, text=operator, fg='white', bg='dark orange', font=('Arial', 15), width=5, height=2, bd=5, relief=GROOVE, command=lambda operator=operator: button_click(operator))
    bt.place(x=(70 * i), y=270)

bt_delete = Button(root, text='Delete', fg='white', bg='red', font=('Arial', 15), width=24, height=1, bd=5, relief=GROOVE, command=clear_display)
bt_delete.place(x=0, y=325)

display = Entry(root, width=30, borderwidth=15)
display.pack()

root.mainloop()