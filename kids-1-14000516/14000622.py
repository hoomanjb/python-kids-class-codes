score = 0
attempt = 5

user_name = input('plz enter your name: ')
print(f'welcome {user_name} to our game, plz answer the questions... ')


def check_answer(guest1, answer):
    global score
    global attempt
    if guest1 == answer:
        score += 1
        print(f'correct answer, your score is {score}')

guest1 = input('what is the biggest animal on the land? ')
check_answer(guest1, 'elephant')

guest2 = input('what is the biggest animal in water? ')
check_answer(guest2, 'whale')

guest3 = input('what  was the name of the bird that could not fly, and got extinct in the 17th century ')
check_answer(guest3, 'dodo')

guest4 = input('what is the tallest animal in the world ')
check_answer(guest4, 'giraffe')

guest5 = input('what is the fastest bird in the world? ')
check_answer(guest5, 'hawk')

print(f'Its DOne your finaly score is {score}')





