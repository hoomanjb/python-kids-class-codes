# Sang kaghaz ghyechi - best of 5
import random

pc_score = 0
user_score = 0
equal_score = 0
select_choice = ['sang', 'kaghaz', 'gheychi']


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

che_tedad = int(input('begoo chand bar: '))

for _ in range(che_tedad):
    pc_choice = random.choice(select_choice)
    # user_choice = input('select (sang, kaghaz, gheychi): ')
    user_choice = random.choice(select_choice)
    result = how_is_winner(pc_choice, user_choice)
    if result == 0:
        print(f'pc choice was: {pc_choice} and user choice was {user_choice}')
        print('result is Equal')
        print(f'user score is: {user_score}')
        print(f'pc  score is {pc_score}')
        equal_score += 1
    elif result == 1:
        print(f'pc choice was: {pc_choice} and user choice was {user_choice}')
        print('result is pc is Winner')
        print(f'user score is: {user_score}')
        pc_score += 1
        print(f'pc  score is {pc_score}')
    else:
        print(f'pc choice was: {pc_choice} and user choice was {user_choice}')
        print('result is User is Winner')
        user_score += 1
        print(f'user score is: {user_score}')
        print(f'pc  score is {pc_score}')

print(50 * '#')
if pc_score > user_score:
    print('Pc is Winner!')
    print(f'Pc Score: {pc_score}')
    print(f'User Score: {user_score}')
    print(f'Equal Score: {equal_score}')

elif pc_score < user_score:
    print('User is Winner!')
    print(f'Pc Score: {pc_score}')
    print(f'User Score: {user_score}')
    print(f'Equal Score: {equal_score}')

else:
    print('You are Equal!')
    print(f'Pc Score: {pc_score}')
    print(f'User Score: {user_score}')
    print(f'Equal Score: {equal_score}')

print(50 * '#')