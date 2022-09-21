import tkinter
import random

window = tkinter.Tk()

window.geometry('600x600')

window.title('Sang Kaghaz Gheychi Game')

user_score = 0
ai_score = 0
user_choice = ''
ai_choice = ''


def show_result():
    global user_choice
    global ai_choice
    global user_score
    global ai_score
    if user_choice == ai_choice:
        print('MOSAVI!')
    elif (user_choice == 'sang' and ai_choice == 'gheychi') or (user_choice == 'kaghaz' and ai_choice == 'sang') or (user_choice == 'gheychi' and ai_choice == 'kaghaz'):
        print('User barandas')
        user_score += 1
    elif (ai_choice == 'sang' and user_choice == 'gheychi') or (ai_choice == 'kaghaz' and user_choice == 'sang') or (ai_choice == 'gheychi' and user_choice == 'kaghaz'):
        print('Ai barandas')
        ai_score += 1

    text_box = tkinter.Text(window, height=50, width=50)
    text_box.grid(row=3, column=1)
    message = f"""
shoma dokmeye {user_choice}
ai dokmeye {ai_choice}

pas emtiaze  shoma mishe {user_score}
emtiaze ai mishe {ai_score}
"""
    text_box.insert(tkinter.END, message)


def sang_clicking():
    global user_choice
    global ai_choice
    user_choice = 'sang'
    ai_choice = random.choice(['sang', 'kaghaz', 'gheychi'])
    show_result()


def kaghaz_clicking():
    global user_choice
    global ai_choice
    user_choice = 'kaghaz'
    ai_choice = random.choice(['sang', 'kaghaz', 'gheychi'])
    show_result()


def gheychi_clicking():
    global user_choice
    global ai_choice
    user_choice = 'gheychi'
    ai_choice = random.choice(['sang', 'kaghaz', 'gheychi'])
    show_result()


sang_button = tkinter.Button(
    window, text=' SANG ', bg='skyblue',
    width=10, command=sang_clicking
)
sang_button.grid(row=1, column=0)

kaghaz_button = tkinter.Button(
    window, text=' KAGHAZ ', bg='pink',
    width=10, command=kaghaz_clicking
)
kaghaz_button.grid(row=1, column=1)

gheychi_button = tkinter.Button(
    window, text=' GHEYCHI ', bg='lightgreen',
    width=10, command=gheychi_clicking
)
gheychi_button.grid(row=1, column=2)

window.mainloop()
