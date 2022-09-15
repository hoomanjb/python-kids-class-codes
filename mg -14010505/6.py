# LOOP - While For

# name = 'hooman'
# for item in name:
#     print(item)

# my_list = [1, 2, 4, 6, 'test', 'salam', [5, 8]]
#
# for item in my_list:
#     print(item)
# a = 1
# print('Start')
# while a < 100:
#     if a % 2 == 0:   # even
#         print(a)
#     a = a + 1
# print('End')

# for item in range(0, 100):
#     print(item)
#     print('Start')
#     if item % 2 != 0:
#         print(f'{item} is odd')
#         continue
#     elif item == 50:
#         print('End!!!!!')
#         break
#     else:
#         print(f'{item} is even')
#     print('End')

# #########################################3
#  multiplication 1 to 10
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
#
#
# 10 20 30 40 50 60 70 80 90 100
# (3*1) (3*2) (3*3) (3*4) (3*5) (3*6) (3*7) (3*8) (3*9) (3*10)
# a = 'salam'
# b = 30
# c = [4, 6, 8]
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(x * y)

# print('Start')
# name = input('plz enter your name: ')
# age = input('plz enter your age: ')
#
# print(name)
# print(age)


# #########################################
# Guess the words
# 9 lives
# ? ? ? ? ?  -> apple
# a -> a ? ? ? ?
# z -> a ? ? ? ? -> 8 lives
# p -> app??

# print('Start Game')
# lives = 9
# print('Guess the words ')
# word = 'apple'
# word_len = len(word)
# result = '? ' * word_len
# result = result.split()
# print(result)
# while lives > 0:
#     if '?' not in result:
#         print('Good Job! You Win')
#         print(word)
#         break
#     user_input = input('plz enter a char: ')
#     if user_input in word:
#         print('Correct!')
#         index = 0
#         for item in word:
#             if word[index] == user_input:
#                 result[index] = user_input
#             index += 1
#         print(result)
#     else:
#         print('Incorrect')
#         lives -= 1








