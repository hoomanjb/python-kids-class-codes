# {}  Angle Brackets - Curly Brackets
# []  Square Brackets - Box Brackets
# ()  Parentheses - Round Brackets - Brackets
# <>  Arrow - Angle Brackets - Chevrons
# =   equal
# /   slash
# -   dash  _ underscore underline
# *   star   ^ hat
# !   Exclamation mark
# ' " ,  :  \  /  %  +
# Comment Shortcut   ctrl+/
# * multi  / division  - subtraction + addition

# a = 10
# a = a + 5
# a += 5
# a -= 5 # a = a - 5
# a /= 5 # a = a / 5
# a *= 5 # a = a * 5
# print(a)

# a = 7
# b = 7
# < > == <= >=
# print(a < b)
# print(a <= b)
# a = 7
# b = 10
# c = 3
# and
# 0 0  -> 0
# 0 1  -> 0
# 1 0  -> 0
# 1 1  -> 1

# or
# 0 0  -> 0
# 0 1  -> 1
# 1 0  -> 1
# 1 1  -> 1

# print(a < c and b > a)
# print(a < c or b > a)

# print(a > b and (b < c or a == a))
# print(a > b and b < c or a == a)

# print(not a == a)

# ##############################3
# Boolean
# True -> 1 ' ' [1, 2]
# False -> 0  '' []
# a = True
# print(type(a))
# print(bool(0))
# print(bool(1))
# print(bool(''))
# print(bool(' '))

# ##################################
# String
# a = 'hello'
# b = "hello"
# print(type(a))
# print(type(b))
# phone_number = '321549812754'

# c = 'hello"world'
# d = "hello" "world"
# print(d)

# a = 'hello '
# b = 'world'
# c = a + b
# d = a * 10
# print(c)
# print(d)

# a = 'hello worldsdlkajbfasldjbflasjdhbflajsdbkajsbfkajsbfkasjbfasdkjbf'
#    012345678910
# print(a[0])
# print(a[6])
# print(a[10])
# print(a[-1])
# print(a[-2])

# b = '123123123'
#
# print(len(b))  # 11 - 10

# a = 'hello worldsdlkajbfasldjbflasjdhbflajsdbkajsbfkajsbfkasjbfasdkjbf'
# print(a[0:10]) # a[start:end:step]
# print(a[10:30])
# print(a[:5])
# print(a[40:])
# print(a[:20])
# print(a[:20:5])

# a = 'heloo'  # ooleh
# print(a)
# print(a[:])
# print(a[4:0:])
# print(a[::-1])

# print('#' * 40)

# a = 'hello'
# b = ' '
# c = 'world'
# a, b, c = 'hello', ' ', 'world'
# print(a + b + c)
# a = 'A'
# b = 'a'
# print(a == b)

# word = 'hello'
# print('lo' in word)
# print('z' not in word)

# user_input = input('plz send me your name: ')
#
# print('your name is: ' + user_input)

# text = 'hello welcome to our class\nmy name is\t hooman\nIm your\b teacher'
# \d \t \b
text = '''
hello welcome" to our class
my' name is hooman
Im your teacher
'''
print(text)


