import tkinter as tk
import random

window = tk.Tk()
window.geometry('400x400')
window.title('Sang Kaghaz Gheychi Game')

user_score = 0
ai_score = 0
user_choice = ''
ai_choice = ''
result = ''

def how_is_winner(pc, user):
    # result -> 0 = equal , 1 = pc , 2 = user
    if pc == user:
        return 0
    elif pc == 'kaghaz':
        if user == 'sang':
            return 1  # pc is winner
        else:
            return 2  # user is winner
    elif pc == 'sang':
        if user == 'kaghaz':
            return 2  # user is winner
        else:
            return 1  # pc is winner
    elif pc == 'gheychi':
        if user == 'kaghaz':
            return 1  # pc is winner
        else:
            return 2  # user is winner

# a = {'sang': 0, 'kaghaz': 1, 'gheychi': 2}
# b = {0: 'sang' , 1: 'kaghaz' , 'gheychi': 2}


def set_random_ai_choice():
    return random.choice(['sang', 'kaghaz', 'gheychi'])


def show_result(user_choice, ai_choice):
    global ai_score
    global user_score
    global result
    winner = how_is_winner(ai_choice, user_choice)
    if winner == 0:
        result = 'Mosavi'
    elif winner == 1:
        ai_score += 1
        result = 'Ai is Winner...'
    else:
        result = 'User is winner'
        user_score += 1
    message = f"""
    {result}

    your choice is {user_choice}
    ai choice is {ai_choice}

    your score is {user_score}
    ai score is {ai_score}
    """
    text_box.delete("1.0", "end")
    text_box.insert('0.0', message)




def sang():
    global user_choice
    global ai_choice
    user_choice = 'sang'
    ai_choice = set_random_ai_choice()
    show_result(user_choice, ai_choice)


def kaghaz():
    global user_choice
    global ai_choice
    user_choice = 'kaghaz'
    ai_choice = set_random_ai_choice()
    show_result(user_choice, ai_choice)


def gheychi():
    global user_choice
    global ai_choice
    user_choice = 'gheychi'
    ai_choice = set_random_ai_choice()
    show_result(user_choice, ai_choice)


sang_button = tk.Button(text='Sang', bg='skyblue', width=10, command=sang)
sang_button.grid(row=1, column=0)

kaghaz_button = tk.Button(text='Kaghaz', bg='lightgreen', width=10, command=kaghaz)
kaghaz_button.grid(row=1, column=1)

gheychi_button = tk.Button(text='Gheychi', bg='pink', width=10, command=gheychi)
gheychi_button.grid(row=1, column=2)

text_box = tk.Text(master=window, height=15, width=30, bg='gray', font='arial')
text_box.grid(row=2, column=1)
text_box.insert(tk.END, '')


window.mainloop()




# a = print()
# b = print
# print(a)
# print(b)

# b = print
# b('salam')
# print('salasdasdasdaam')

