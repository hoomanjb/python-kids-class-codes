# Password Picker
# تعداد کارکترهای پسورد چنتا باشد؟ بله)0 خیر)1
# آیا از اعداد استفاده شود؟ بله)0 خیر)1
# آیا حروف کوچک انگلییسی داشته باشد؟ بله)0 خیر)1
# آیا حروف کوچک انگلییسی داشته باشد؟ بله)0 خیر)1
# آیا از حروف مخصوص مثل: /!@#$%^&*)( استفاده شود؟ بله)0 خیر)1

# print('a^123')
import random

# answer1 = input('تعداد کارکترهای پسورد چنتا باشد؟  ')
answer2 = input('آیا از اعداد استفاده شود؟ 0-بله 1-خیر ')
answer3 = input('آیا حروف کوچک انگلییسی داشته باشد؟ 0-بله 1-خیر ')
answer4 = input('آیا حروف بزرگ انگلییسی داشته باشد؟ 0-بله 1-خیر ')
answer5 = input('آیا از حروف مخصوص مثل: /!@#$%^&*)( استفاده شود؟ 0-بله 1-خیر ')

words2 = '0123456789'
words3 = 'qwertyuiopasdfghjklzxcvbnm'
words4 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
words5 = '/!@#$%^&*)('

result = ''

if answer2 == '0':
    a = random.choice(words2)
    result += a

if answer3 == '0':
    a = random.choice(words3)
    result += a

if answer4 == '0':
    a = random.choice(words4)
    result += a

if answer5 == '0':
    a = random.choice(words5)
    result += a


print(result)

# while , for  -> loop
