# name = input(' enter your name : ')
# number_error = 0
# boolean_name = name.isalpha()
# if boolean_name == True:
#     print(' welcome ', name)
#
# while boolean_name == False:
#     number_error += 1
#     if number_error == 3:
#         print('Sorry, your input is too high . Do we are your ridiculous?????????:((')
#         break
#     print('Error , please enter just alphabet and you cant enter more than 3 times')
#     name = input(' enter your name again: ')
#     boolean_name = name.isalpha()
#     if boolean_name == True:
#         print(' welcome ', name)
#     else:
#         continue

# ##########################################################
while True:
    name = input(' enter your name : ')
    if name.isalpha():
        print('hello welcome ', name)
        break
    else:
        print('IS WRONGGGG!!!!!! TRY AGAIN')

user_score = 0
question1 = '1- bozorgtarin heyvan khoshki chist? : '
question2 = '2- bozorgtarin heyvan daryaii chist? : '
question3 = '3- aya morgh parvaz mikonad ya kheir? : '
question4 = '4- kodom bozorg tar ast 2 ya 5 ? : '
question5 = '5- natije ebarate roo b roo a == b ba yes or no javab dahid? : '

number_error = 0
while True:
    answer = input(question1)
    if answer == 'fil':
        user_score += 1
        print('afarin javabet doros bood emtiazet shode: ', user_score)
        break
    else:
        number_error += 1
        if number_error == 3:
            print('tamami shans hato baraye in soal az dast dadi javabe sahih: fil')
            break
        else:
            print('eshtebah javad dadi dobare talash kon!')

number_error = 0
while True:
    answer = input(question2)
    if answer == 'wall':
        user_score += 1
        print('afarin javabet doros bood emtiazet shode: ', user_score)
        break
    else:
        number_error += 1
        if number_error == 3:
            print('tamami shans hato baraye in soal az dast dadi javabe sahih: wall')
            break
        else:
            print('eshtebah javad dadi dobare talash kon!')

number_error = 0
while True:
    answer = input(question3)
    if answer == 'no':
        user_score += 1
        print('afarin javabet doros bood emtiazet shode: ', user_score)
        break
    else:
        number_error += 1
        if number_error == 3:
            print('tamami shans hato baraye in soal az dast dadi javabe sahih: no')
            break
        else:
            print('eshtebah javad dadi dobare talash kon!')


number_error = 0
while True:
    answer = input(question4)
    if answer == '5':
        user_score += 1
        print('afarin javabet doros bood emtiazet shode: ', user_score)
        break
    else:
        number_error += 1
        if number_error == 3:
            print('tamami shans hato baraye in soal az dast dadi javabe sahih: 5')
            break
        else:
            print('eshtebah javad dadi dobare talash kon!')

number_error = 0
while True:
    answer = input(question5)
    if answer == 'no':
        user_score += 1
        print('afarin javabet doros bood emtiazet shode: ', user_score)
        break
    else:
        number_error += 1
        if number_error == 3:
            print('tamami shans hato baraye in soal az dast dadi javabe sahih: no')
            break
        else:
            print('eshtebah javad dadi dobare talash kon!')






