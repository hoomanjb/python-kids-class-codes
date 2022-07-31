score = 0
mistakes = 0

user_name = input("Hi! welcome to this animal quiz game, inorder to play this game you need to type your name! ")
print(f'Hi {user_name} and welcome to this game. Goodluck!')
x = input('To start, press any key and press enter, and if you wish to exit, type exit! ')

def start():
    global score
    global mistakes
    while 1:
        x = input('What is the largest sea animal? ')
        if x == 'blue whale':
            score += 1
            print('Correct!')
            break
        else:
            mistakes += 1
            print('Incorrect! Try again!')
            continue

    while 1:
        x = input('What is the most endangered animal? ')
        if x == 'javan rhinoceros':
            score += 1
            print('Correct!')
            break
        else:
            mistakes += 1
            print('Incorrect! Try again!')
            continue

    while 1:
        x = input('What is the tallest animal? ')
        if x == 'giraffe':
            score += 1
            print('Correct!')
            break
        else:
            mistakes += 1
            print('Incorrect! Try again!')
            continue

    while 1:
        x = input('What is the fastest bird in the world? ')
        if x == 'peregrine':
            score += 1
            print('Correct!')
            break
        else:
            mistakes += 1
            print('Incorrect! Try again!')
            continue

    while 1:
        x = input('What is the fastest animal in the world? ')
        if x == 'cheetah':
            score += 1
            print('Correct!')
            break
        else:
            mistakes += 1
            print('Incorrect! Try again!')
            continue

    print(f'Good job! Your final score was {score}, and you got {mistakes} mistakes!')
    print('Goodbye!')

while 1:
    if x == 'exit':
        print('Goodbye!')
        break
    else:
        start()
        break