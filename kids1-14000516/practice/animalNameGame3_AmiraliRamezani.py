#######AmiraliRamezani###############
#######AnimalNameGame################
#######Anisa#########################
import time
import turtle

point = 0
chance = 6
Q = [['1- what is the biggest animal on the land?', 'elephant']
    , ['2- what is the biggest animal in water?', 'whale']
    , ['3- what  was the name of the bird that could not fly, and got extinct in the 17th century', 'dodo']
    , ['4- what is the tallest animal in the world', 'giraffe']
    , ['5- what is the fastest bird in the world?', 'hawk']
    , ['6- which group of animal has the most population on earth?', 'insects']]


def QandA(index, qaList):
    return qaList[index]


#################START GAME#########
while 1:
    s = input(' hello and welcome to this game, for start, type start and for exit, type, exit')
    if s == 'exit':
        print('bye')
        break

    elif s == 'start':
        counter = 0
    while 1:
        tempList = list(QandA(counter, Q))
        question = str(tempList[0])
        answer = input(question)

        if answer == tempList[1]:
            print("Correct")
            point += 1
            if counter == len(Q) - 1:
                print('congratulations, you answered correctly to every single question')
                time.sleep(1.5)
                print(f'you have managed to get {point} points! Good Job')
                break
            else:
                counter += 1

        elif answer == 'exit':
            print(' ok, bye ')
            break

        else:
            print('false')
            chance -= 1
            if chance == 0:
                print(' GAME OVER ')
                break
            else:
                print(f' now you have {chance} chances')
