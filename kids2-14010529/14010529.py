import random

# num_list = list(range(1, 51))
# goal = random.choice(num_list)

goal = random.randint(1, 50)

# goal = 37

print('Start The Game')

while True:
    user_input = input('yek adad beyne 1 ta 50 hads bezan: ')
    if user_input.isdecimal():
        if int(user_input) == goal:
            print('dorost hads zadid!!!')
            print(f'javabe sahih {goal} ast')
            break

        elif int(user_input) < goal:
            print(f'adad bishtari ra az {user_input} entekhab kon')

        elif int(user_input) > goal:
            print(f'adad kamtari ra az {user_input} entekhab kon')

    else:
        print('gharar bood faghad adad bedi behem!!!')
