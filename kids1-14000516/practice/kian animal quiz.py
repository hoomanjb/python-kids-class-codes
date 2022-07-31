#پروژه کیان مرادی
def name_getting():
    user_name = input('please enter your username:')
    print(f'welcome to the to the animal quiz {user_name},you have to find the correct answer to the 5 questions and you have 10 chances.good luck.')
chances = 10
score = 0
def question_check(user_answer, correct_answer):
    global chances
    global score
    if chances == 0:
        return 0
    elif user_answer == 'next':
        print('are you sure? you will lose this question point:')
        user_answer = input('write yes if you want to continue:')
        if user_answer == 'yes':
            return 0
        else:
            return 1
    elif user_answer == correct_answer:
        print('correct,you get a point,going to a next question')
        score += 1
        return 0
    else:
        print('wrong answer,try again')
        chances -= 1
        return 1

def main(question, answer):
    while 1:
        user_answer = input(question)
        a = question_check(user_answer, answer)
        if not a:
            break

name_getting()

while 1:
    main('1st question:what is the biggest animal?', 'blue whale')
    if chances == 0:
        break
    main('2nd question:what is the tallest land animal?', 'giraffe')
    if chances == 0:
        break
    main('3rd question:what is the biggest land animal?', 'elephant')
    if chances == 0:
        break
    main('4th question:what is the biggest bird? 1_ ostrich 2_ eagle 3_vulture?', 'ostrich')
    if chances == 0:
        break
    main('5th question:what is the fastest animal? 1_cheetah 2_eagle 3_falcon?', 'falcon')
    if chances == 0:
        break
    if chances > 0:
        print('thank you for participating in this test')
        print('your score was...')
        print(score)
        print(f'{chances} chances were left')
        print('have a nice day')
        a = input('if you want to exit write out:')
        if a == 'out':
            break
while 1:
    a = input(f'you lost your chances, your score was {score},to exit the test write out:')
    if a == 'out':
        break
    else:
        print('I didnt understand')
#kian moradi's project

