# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(a[1])
# a[0] -> 1
# b[:] -> []
# a[0] * b[0] = 1 * 1 -- a[0] * b[1] = 1 * 2 --- a[0] * b[-1] = 1 * 10

# index_a = 0
# while index_a <= 9:
#     x = a[index_a]
#     if x == 5:
#         index_a += 1
#         continue
#     index_b = 0
#     result = ''
#     while index_b <= 9:
#         y = b[index_b]
#         result += f'{x*y:^3} '
#         # result += f'{x*y:<3} '
#         index_b += 1
#     print(result)
#     index_a += 1

# index_a = 1
# while index_a <= 10:
#     index_b = 1
#     while index_b <= 10:
#         result = index_a * index_b
#         print(result)
#         index_b += 1
#     index_a += 1


# #######################################
# list = ['?','?','?','?','?']
# print(list)
# while True:
#     if list == ['m','a','h','a','n']:
#         print("afarin")
#         print('javab *mahan* bood')
#         break
#     data = input('ye harf bego:')
#     if data == 'm':
#         list[0] = 'm'
#         print(list)
#     elif data == 'a':
#         list[1] = 'a'
#         list[3] = 'a'
#         print(list)
#     elif data == 'h':
#         list[2] = 'h'
#         print(list)
#     elif data == 'n':
#         list[4] = 'n'
#         print(list)
#     else:
#         print('No')

# ###############################33
import random

words = ['apple', 'orange', 'car', 'cat', 'benz']
word = random.choice(words)
word = 'apple'
counter = 1
select_list = []
while counter <= len(word):
    select_list.append('?')
    counter += 1

print('Start Game:')
live = 10
while live >= 1:
    print(select_list)
    if '?' not in select_list:
        print('Shoma barande Shodid')
        break
    user_input = input(' yek harf b joz adad hads bezan(a-z) :')
    if user_input in word:
        print('dorost hads zadi!')
        index = 0
        while index < len(word):
            if user_input == word[index]:
                select_list[index] = user_input
            index += 1
                # select_list[index] = word[index]
    else:
        print('eshtebah javab dadi.')
        live -= 1
        print(f' tedade joone baghi mande {live} ast')

print('End')



