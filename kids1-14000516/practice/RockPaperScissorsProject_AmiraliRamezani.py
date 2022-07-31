import random


username = input('what is your user name?')

while True:
    start = input(f'hello {username}, welcome to this game! 1- Start 2-Exit ')
    ai_point = 0
    player_point = 0

    if start == '1':
        print('lets go!')
        player_move = input('choose between rock, paper  or scissors')
        ai_choice = ['rock', 'paper', 'scissors']
        ai_move = random.choice(ai_choice)
        print(ai_move, 'vs', player_move)

        if ai_move == player_move:
            print('it is a draw!')
            print(f' {username}: {player_point}, AI: {ai_point} ')

        elif ai_move == 'rock' and player_move == 'paper':
            print(f'{username} won!')
            player_point += 1
            print(f' {username}: {player_point}, AI: {ai_point} ')

        elif ai_move == 'paper' and player_move == 'rock':
            print('AI won!')
            ai_point += 1
            print(f' {username}: {player_point}, AI: {ai_point} ')

        elif ai_move == 'scissors' and player_move == 'rock':
            print(f'{username} won!')
            player_point += 1
            print(f' {username}: {player_point}, AI: {ai_point} ')

        elif ai_move == 'rock' and player_move == 'scissors':
            print(' AI won!')
            ai_point += 1
            print(f' {username}: {player_point}, AI: {ai_point} ')

        elif ai_move == 'paper' and player_move == 'scissors':
            print(f'{username} Won!!')
            player_point += 1
            print(f' {username}: {player_point}, AI: {ai_point} ')

        elif ai_move == 'scissors' and player_move == 'paper':
            print(' AI won! ')
            ai_point += 1
            print(f' {username}: {player_point}, AI: {ai_point} ')

        else:
            print(' an error occurred, please repeat')


    elif start == '2':
        print('OK, bye!')
        break
    else:
        c = print('Try Again')
