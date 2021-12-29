point = 0

chance = 9
correct_message = 'well done! now you have {} point'
wrong_message = f'it\'s wrong... you have {chance} chance. please try again!'
questions = ['animal that walk slowly and has short legs.it also live in sea and earth :', 
    'animal that has long neck and eat plant : ',
    'animal that sleep 20 hours in day: ',
    'animal that is smart and eat carret: ',
    'animal that have big ears and is so heavy: ']
answers = ['turtle', 'giraffe', 'koala bear', 'rabit', 'elephant']
x = 10

def start():
    global chance
    global point
    for x in questions:
        for z in answers:
            answer = input(x)
            if answer == 'exit':
                print('bye bye')
                break
            elif chance == 0:
                print('you lose')
                break
            elif answer == z:
                point =+ 1
                print(correct_message)
                break
            elif answer != z or answer != 'exit':
                chance =- 1
                print(wrong_message)

          
name = input('please enter your name :')
print((f'Hi {name}! Welcome to animal game... We give you some information about animal '
     'and then you should gusse it! please type "start" to START or "exit" to EXIT : '))

join = 10

while 1994:
    join = input('')
    if join == 'exit':
        break
    elif join == 'start' :
        start()
    elif join != 'start' or join !='exit' :
        print('please type a true letter')
