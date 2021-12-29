def check_answer(q1, answer):
    global score
    global attempt
    if q1 == answer:
        score += 1
        print(f'your answer is correct!,score:{score}')
    else:
        print('its not correct!')


while True:
    score = 0
    attempt = 5
    e = input('please enter your name: ')
    z = input(f'wellcome {e} to general information test,type start when you are ready to start the test!')
    if z == 'start':
        print('lets go!')
    else:
        print('try when you are ready!')
        break
    q1=input('what element humans use to make processors?')
    check_answer(q1,"silicon")

    q2=input('who wrote python?')
    check_answer(q2, "Van Rossum")

    q3=input('who invented the original car?')
    check_answer(q3, 'carl benz')

    q4=input("who is the CEO of nvidia company?")
    check_answer(q4, 'Jensen Huang')

    q5=input('where is intel company from?')
    check_answer(q5,'usa')

    print(f'Its done! score:{score}')