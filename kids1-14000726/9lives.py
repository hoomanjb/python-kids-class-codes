import random

count_heart = 9
user_chance = count_heart * u'\u2764'

def make_incomplete_word(word):
    # ['?','?','?','?','?']
    result = []
    for item in word:
        result.append('?')
    return result

def random_exam_choice():
    exam = ['PITZZA', 'WINDOW', 'TEETH', 'ANISA', 'SHIRT', 'NIGHT']
    random_choice = random.choice(exam)
    return random_choice

def getting_user_name():
    while True:
        name = input(' enter your name : ')
        if name.isalpha():
            return name
        else:
            print('IS WRONGGGG!!!!!! TRY AGAIN')

def check_word_by_char(user_char, word, incomplete_word):
    if user_char in word:
        index = 0
        for item in word:
            if user_char == item:
                incomplete_word[index] = user_char
                # ['?', e, e, '?','?'] -> teeth
            index += 1
        return incomplete_word
    else:
        return False

user_name = getting_user_name()

while True:
    print(20 * "*")
    print(f"Welcome To 9Lives Game mr/miss {user_name}")
    print()
    print('MAIN MENU')
    print('CHOOSE FROM MENU:')
    print('1- Start GAME: ')
    print('2- Show Lives: ')
    print('3- Exit')
    selected_menu = input()
    if selected_menu == '3':
        print('By By')
        break
    elif selected_menu == '2':
        print(f"your Lives is: {user_chance}")
        print()
        continue
    elif selected_menu == '1':
        random_word = random_exam_choice()
        incomplete_word = make_incomplete_word(random_word)
        while True:
            print(incomplete_word)
            print('ye charchter hads bezan: ')
            selected_char = input()
            result = check_word_by_char(selected_char.upper(), random_word, incomplete_word)
            if result:
                print('dorost entekhab kardi hal nobate hadse baadite')
                incomplete_word = result
                continue

            else:
                print('eshtebah hads zadi va 1 joon az dast midi')
                count_heart -= 1
                user_chance = count_heart * u'\u2764'
                print(user_chance)
    else:
        print('Please Selecet From Menu 1 to 3...!')
        continue


