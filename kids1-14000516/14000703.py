import random
import string

# adj = ['sleepy', 'fat', 'Slow', 'wet', 'brave', 'Orange', 'pink', 'green', 'blue',
#        'dry', 'bad', 'Fast', 'Exited', 'Happy', 'depressed']
#
# noun = ['aPple', 'Hammer', 'Goat', 'panda', 'ball', 'toaster']
#
# special_char = ['~', '!', '#', '$', '^', '&', '(']
#
# number = random.randrange(0, 100)
#
# selecet_adj = random.choice(adj)
#
# selected_noun = random.choice(noun)
#
# selcted_special_char = random.choice(special_char)
#
# result = ''
# for item in range(4):
#     number = random.randrange(0, 100)
#     selecet_adj = random.choice(adj)
#     selected_noun = random.choice(noun)
#     selcted_special_char = random.choice(special_char)
#     result += f'{number}{selecet_adj}{selected_noun}{selcted_special_char}'
#
#
# print(result)


pass_lenght = int(input('enter password lenght: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special_char = string.punctuation

result = lower + upper + numbers + special_char

temp_pass = random.sample(result, pass_lenght)

print(''.join(temp_pass))

