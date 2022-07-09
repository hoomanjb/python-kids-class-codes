# import string
# import random
#
#
# def password(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
#     return ''.join(random.choice(chars) for _ in range(size))
#
#
# print(password(int(input('How many characters in your password? '))))



# import random
#
# answer1 = input('تعداد کارکترهای پسورد چنتا باشد؟  ') # 10
# answer2 = input('آیا از اعداد استفاده شود؟ 0-بله 1-خیر ') # 1
# answer3 = input('آیا حروف کوچک انگلییسی داشته باشد؟ 0-بله 1-خیر ') # 1
# answer4 = input('آیا حروف بزرگ انگلییسی داشته باشد؟ 0-بله 1-خیر ') # 1
# answer5 = input('آیا از حروف مخصوص مثل: /!@#$%^&*)( استفاده شود؟ 0-بله 1-خیر ') # 1
#
# words2 = '0123456789'
# words3 = 'qwertyuiopasdfghjklzxcvbnm'
# words4 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# words5 = '/!@#$%^&*)('
#
# answers = [answer1, answer2, answer3, answer4, answer5]
#
#
# def make_password(user_answers):
#     result = ''
#     for item in range(int(answers[0])):
#         if user_answers[1] == '0':
#             result += random.choice(words2)
#         if user_answers[2] == '0':
#             result += random.choice(words3)
#         if user_answers[3] == '0':
#             result += random.choice(words4)
#         if user_answers[4] == '0':
#             result += random.choice(words5)
#
#     return result[:int(answers[0])]
#
# print(make_password(answers))

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
#
#
# for item in my_list:
#     print(item + 5)
#     print(item - 1)
#     print('#############')



import random

lives = 9
words = ['bastani', 'apple', 'orange', 'book', 'pizza']

selected_word = random.choice(words)
clue_list = list('?' * len(selected_word))

def check_answer(answer):
    flag = False
    if answer in selected_word:
        index = 0
        for item in selected_word:
            if item == answer:
                flag = True
                clue_list[index] = answer
            index += 1
    return flag

selected_word = 'book'
clue_list = list('?' * len(selected_word))
print(clue_list)
check_answer('o')
print(clue_list)

# user_input = input('yek harf vared konid?')

