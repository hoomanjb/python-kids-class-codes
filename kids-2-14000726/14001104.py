# while True:
#     name = input(' enter your name : ')
#     if name.isalpha():
#         print('hello welcome ', name)
#         break
#     else:
#         print('IS WRONGGGG!!!!!! TRY AGAIN')
#
# question = ['bozorgtarin heyvan khoshki chist?', 'bozorgtarin heyvan daryaii chist?',
#             'aya morgh parvaz mikonad ya kheir?', '4- kodom bozorg tar ast 2 ya 5 ? ',
#             '5- natije ebarate roo b roo a == b ba yes or no javab dahid? :']
# answers = ['fill', 'wall', 'no', '5', 'no']
# user_score = 0
# for x in range(4):
#     number_error = 0
#     while True:
#         answer = input(str(x + 1) + ' ' + question[x])
#         if answer == answers[x]:
#             user_score += 1
#             print('afarin javabet doros bood emtiazet shode: ', user_score)
#             break
#         else:
#             number_error += 1
#             if number_error == 3:
#                 print('tamami shans hato baraye in soal az dast dadi javabe sahih: ', answers[x])
#                 break
#             else:
#                 print('eshtebah javad dadi dobare talash kon!')

# ##########################################################

# while True:
#     name = input(' enter your name : ')
#     if name.isalpha():
#         print('hello welcome ', name)
#         break
#     else:
#         print('IS WRONGGGG!!!!!! TRY AGAIN')
# user_score = 0
# list1 = ['1- bozorgtarin heyvan khoshki chist? : ', '2- bozorgtarin heyvan daryaii chist? : ',
#          '3- aya morgh parvaz mikonad ba yes or no javab dahid? :', '4- kodom bozorg tar ast 2 ya 5 ? :',
#          '5- natije ebarate roo b roo a == b ba yes or no javab dahid? : ']
# list2 = ['fil', 'wall', 'no', '5', 'no']
# number_error = 0
# item1 = 0
# while True:
#     for item in range(item1, 5):
#         answer = input(list1[item])
#         for item2 in range(item, 5):
#             true = list2[item2]
#             if answer == true:
#                 user_score += 1
#                 print('afarin javabet doros bood emtiazet shode: ', user_score)
#                 break
#             else:
#                 number_error += 1
#             if number_error == 3:
#                 print('tamami shans hato baraye in soal az dast dadi javabe sahih:', true)
#                 break
#             else:
#                 print('eshtebah javad dadi dobare talash kon!')
# #############################################################
# define
# def sum_to_number(x, y):
#     z = (x*y) + 10
#     return z
#
# a = sum_to_number(2, 3)
# print(a)
#
# a1 = sum_to_number(5, 2)
# print(a1)
#
# a2 = sum_to_number(1, 4)
# print(a2)
#
# a3 = sum_to_number(2, 6)
# print(a3)

# ########################################

# def getting_input(message):
#     user_input = input(message)
#     return user_input
#
#
# def check_answer(user_answer, currect_answer, user_score, number_error):
#     if user_answer == currect_answer:
#         user_score += 1
#         print('afarin javabet doros bood emtiazet shode: ', user_score)
#     else:
#         number_error += 1
#         if number_error == 3:
#             print('tamami shans hato baraye in soal az dast dadi javabe sahih: ', currect_answer)
#         else:
#             print('eshtebah javad dadi dobare talash kon!')
#     return user_score, number_error
#
#
# while True:
#     name = getting_input(' enter your name : ')
#     if name.isalpha():
#         print('hello welcome ', name)
#         break
#     else:
#         print('IS WRONGGGG!!!!!! TRY AGAIN')
#
# question = ['bozorgtarin heyvan khoshki chist?', 'bozorgtarin heyvan daryaii chist?',
#             'aya morgh parvaz mikonad ya kheir?', '4- kodom bozorg tar ast 2 ya 5 ? ',
#             '5- natije ebarate roo b roo a == b ba yes or no javab dahid? :']
# answers = ['fill', 'wall', 'no', '5', 'no']
# user_score = 0
# for x in range(4):
#     number_error = 0
#     while True:
#         question_message = str(x + 1) + ' ' + question[x]
#         answer = getting_input(question_message)
#
#         user_score, number_error = check_answer(answer, question[x], user_score, number_error)
#
#         if answer == answers[x]:
#             user_score += 1
#             print('afarin javabet doros bood emtiazet shode: ', user_score)
#             break
#         else:
#             number_error += 1
#             if number_error == 3:
#                 print('tamami shans hato baraye in soal az dast dadi javabe sahih: ', answers[x])
#                 break
#             else:
#                 print('eshtebah javad dadi dobare talash kon!')
# ############################################
# صورت سوال: یک بازی بنویسید که اسم کاربر ازش بپرسه و یک منو نمایش بده. به شرح: شروع بازی و نمایش امتیاز و تغییر اسم کاربر و پایان
import random
a = [1, 2, 3, 4]
b = random.choice(a)

def getting_user_name():
    while True:
        name = input(' enter your name : ')
        if name.isalpha():
            print('hello welcome ', name)
            return name
        else:
            print('IS WRONGGGG!!!!!! TRY AGAIN')

user_name = getting_user_name()
user_score = 0
computer_score = 0
while True:
    print('welcome to Sang Kaghaz Gheychi Game ', user_name)
    print('MAIN MENU')
    print('CHOOSE FROM MENU:')
    print('1- Start GAME: ')
    print('2- Show Score: ')
    print('3- Edit Name: ')
    print('4- Exit')
    selected_menu = input()

    if selected_menu == '4':
        print('By By')
        break
    if selected_menu == '3':
        user_name = getting_user_name()
        continue

    if selected_menu == '2':
        print(f'your score is {user_score} and computer score is {computer_score}')
        continue

    if selected_menu == '1':
        pass

    else:
        continue









