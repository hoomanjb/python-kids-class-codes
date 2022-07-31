wrong = 'wrong answer,try again'

score = 0
wrong_answers = 0

while 1:
    print("hello welcome to the animal quiz, in this quiz every correct answer give you one point and in the end you'll get your result.if you wanted to go to your next qusetion write next." )
    a = input('1st question:what is the biggest animal?')
    if a == 'next':
        break
    else:
        if a == 'blue whale':
            print('correct,you get a point')
            score += 1
            break
        else:
            print(wrong)
            wrong_answers += 1
            continue
while 1:
    a = input('2nd question:what is the tallest land animal?')
    if a == 'next':
        break
    else:
        if a == 'giraffe':
            print('correct,you get a point')
            score += 1
            break
        else:
            print(wrong)
            wrong_answers += 1
            continue
while 1:
    a = input('3rd question:what is the biggest land animal?')
    if a == 'next':
        break
    else:
        if a == 'elephant':
            print('correct,you get a point')
            score += 1
            break
        else:
            print(wrong)
            wrong_answers += 1
            continue
while 1:
    a = input('4th question:what is the biggest bird? 1_ ostrich 2_ eagle 3_vulture?')
    if a == 'next':
        break
    else:
        if 'ostrich' in a or '1' in a:
            print('correct,you get a point')
            score += 1
            break
        else:
            print(wrong)
            wrong_answers += 1
            continue
while 1:
    a = input('5th question:what is the fastest animal? 1_cheetah 2_eagle 3_falcon?')
    if a == 'next':
        break
    else:
        if ('falcon' in a) or ('3' in a): # 3_falcon , a == '3'
            print('correct,you get a point')
            score += 1
            break
        else:
            print(wrong)
            wrong_answers += 1
            continue
    print('thank you for participating in this test')
    print('your score was...')
    print(score)
    print('your wrong answers')
    print(wrong_answers)
    print('have a nice day')
    a = input("if you want to close quiz simply write exit:")
    if a == 'exit':
        break




