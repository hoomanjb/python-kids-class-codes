name = input('enter your name: ')
age = int(input('enter your age: '))
city = input('enter your city: ')
gender = input('khanoom ya aqa? ')

if gender == 'aqa':
    text = f'salam khosh amadid aqaye {name} your age is {age} , your city is {city}'
else:
    text = f'salam khosh amadid khanoome {name} your age is {age} , your city is {city}'

print(text)

if age > 20:
    text = 'salam khosh amadid ey javan'
elif age < 20:
    text = 'salam khosh amadid ey nojavan'
elif age > 50:
    text = 'salam khosh amadid ey pirjavan'
else:
    text = 'نمیدونم سنش چیه!!!'

print(text)

if age > 20 and age < 25:
    print('sene shoma beyne 20 ya 25 ast')
elif age > 25 and age < 40:
    print('sene shoma beyne 25 ta 40 ast.')
elif age < 20:
    print('sene shoma az 20 kamtar ast')
else:
    print('نمیدونم چند سالته!!!')