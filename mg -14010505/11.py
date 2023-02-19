# DataType : Numbers, String, Boolean, List, Dict, Tuple, Set
# String

# a = 'Hello'
# b = ' World'
# c = a + b
# print(c)
# print('Hello World')
#
# print(len(c))
# print(c[0])
# print(c[1:6])
# print(c[::3])


name = 'MaGGie'
# print(name.lower())  # lowercase
# print(name.upper())  # uppercase

# a = 'MaGGie'
# b = 'maggie'
# print(a.lower() == b.lower())


# name = 'AAA-BBB-CCC-@@@-111-222'
# print(name.split(sep='-'))

# email = 'test@gmail.com'
# print(email.split(sep='@'))


# text = 'Hello World                '
# print(text.rstrip())
# text = '        Hello World'
# print(text.lstrip())
# text = '        Hello World           '
# print(text.strip())


# text = 'Hello World'
# print(text.index('l'))
# print(text[3:].index('l'))
# print(text.index('W'))
# # print(text.index('z')) Not Good Command(Method)
# print(text.find('z'))


# text = 'Hello World'
# print(text.startswith('G'))
# text = '+1123123123'
# print(text.startswith('+1'))
# print(text.endswith('3'))
# print(text.endswith('@gmail.com'))


# text = 'HEllo'
# print(text.count('l'))


text = 'test@gmail'
# if len(text) == 10:
#     for item in text:
#         if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             print(' Wrong Input!')
# else:
#     print(' This is Wrong!')

# if len(text) == 10 and text.isdigit():  # all Numbers
#     print('ok')
# else:
#     print('Wrong')

# Special Char: ~!@@#$$%^&* ()-+/><
# text = 'helloworld'
# print(text.isalpha())
#
# text = 'hellowo123rld'
# print(text.isalnum())

# a = 'TEST'
# print(a.islower())
# print(a.isupper())

# print(a.replace('E', 'Z'))

# name = 'M  a   g                g    ie'
# result = 'Maggie'
# print(name.replace(' ', ''))


# name = 'Maggie'
# text = f'Hello {name} Welcome To My Web Site.'
# print(text)


# #########################################
# 1. Write a Python program to calculate the length of a string.
# a = 'hello'

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
#
# Sample String : 'w3asdasdasw3'
# Expected Result : 'w3w3'
# Sample String : 'w'
# Expected Result : None

def exam_3(text):
    if len(text) < 2:
        return None
    else:
        return text[:2] + text[-2:]

a = 'w3jkflksjdfgnldkjfgnZ3'
print(exam_3(a))  # w3Z3


