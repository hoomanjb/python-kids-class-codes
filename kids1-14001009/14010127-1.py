# n = 1
# n += 5 # n = n + 5

q1 = 'natijeye moadeleye roo b roo che mishavad ->  3 + 4 = ?  : '
q2 = 'natijeye moadeleye roo b roo che mishavad ->  5 * 2.7 = ?  : '
q3 = 'paytakht iran tehran ast ya kheir:  1)bale  2)kheir  : '

score = 0

answer1 = input(q1)
if int(answer1) == 7:
    score += 1
    print('afarin dorost javab dadi')
    print(f'emtiaze shoma felan shode: {score}')
else:
    print('javabe dorost mishe 7')

answer2 = input(q2)
if float(answer2) == 13.5:
    score += 1
    print('afarin dorost javab dadi')
    print(f'emtiaze shoma felan shode: {score}')
else:
    print('javabe dorost mishe 13.5')

answer3 = input(q3)
if int(answer3) == 1:
    score += 1
    print('afarin dorost javab dadi')
    print(f'emtiaze shoma felan shode: {score}')
else:
    print('javabe dorost mishe 1')



print('bazi tamam shod')
print('emtiaze nahaii shoma shode: ', score)