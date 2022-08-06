# jadval zarb
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# counter1 = 1
# counter2 = 1
#
# while counter1 <= 10:
#     b = counter1 * counter2
# x = 1
# y = 1
# while x <= 10:
#     y = 1
#     result = ''
#     while y <= 10:
#         res = str(x * y)
#         result += f'{res:3}'
#         y += 1
#     print(result)
#     x += 1

# '1   2    3    4    5    6    7    8    9    10'
# '2                                           20'
#
#
# 9                                            90
# 10                                           100

# ######################### ######################### #
import random

my_words = ['apple', 'orange', 'car', 'cat', 'havij']
random_choice = random.choice(my_words)
live = 10
chars_word = len(random_choice)
result = []
counter = 1
while counter <= chars_word:
    result.append('?')
    counter += 1

print(result)
print(" START GAME :")
print(f' YOUR LIVE IS: {live}')
while live >= 1:
    user_input = input('ye harf ro hads bezan (a-z): ')
    if user_input in random_choice:
        print('Dorost Javab dadi!')
        index = 0
        index_list = []
        counter = 1
        while counter <= chars_word:
            if user_input == random_choice[index]:
                index_list.append(index)
            counter += 1
            index += 1
        index = 0
        counter = 1
        while counter <= len(index_list):
            base_index = index_list[index]
            result[base_index] = user_input
            counter += 1
            index += 1
        print(result)
        if '?' not in result:
            print(' AFARIN 100 AFARIN TAMAM SHOD!')
            break
    else:
        live -= 1
        print(f'ESHETAB JAVAD DADI, LIVE: {live}')


print(f'YOUR ANSWER IS: {random_choice}')
print('END GAME')

