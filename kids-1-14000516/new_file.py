while 3:
    name = input("please enter your name : ")
    print(f"welcome to Animal Game, {name}!")
    print("Game Guide : We give you some information about animal, then you should gusse that animal! ")
    print('Please type "start" to START! and type "exit" to EXIT! ')
    start = input("")
    if start == "start":
        print("animal that walk slowly and has short legs.it also live in sea and earth :")
        answer = input("")
        if answer == "turtle":
            print("Well done!")
            print("animal that has long neck and eat plant : ")
            answer = input("")
            if answer == "giraffe":
                print("Well done!")
            else:
                print("please try again...")
                print("animal that walk slowly and have short legs.it also live in sea and earth :")
            answer = input("")
        else:
            print("please try again...")
            print("animal that walk slowly and have short legs.it also live in sea and earth :")
            answer = input("")
    elif start == "exit":
        break

