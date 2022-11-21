# 1 word [1, 2, 3, 4, 5]
# 3 bar try

import random

my_list = ['apple', 'orange', 'cherry', 'carrot', 'blueberry', 'bananas', 'mango', 'avocado', 'pineapple']

goal = random.choice(my_list)
print(goal)
for item in range(3):
    user_input = input(f'plz enter from this list: {my_list}: ')
    if user_input == goal:
        print('Bravo!')
        break
    else:
        print('Incorrect')
        if user_input in my_list:
            my_list.remove(user_input)

print('Game Over')


# test1()
# test2()