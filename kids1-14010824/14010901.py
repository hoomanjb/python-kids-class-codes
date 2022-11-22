# bool منطقی - 0و 1

# a = True
# print(a)
# print(type(a))
# print(bool(0))
# True  -> 1 , ' ', [6]
# False -> 0 , '' , []

# print(bool(''))
# print(bool(' '))

# a = 10
#
# a += 5  # a = a + 5
# a -= 5  # a = a - 5
# a *= 5  # a = a * 5
# a /= 5  # a = a / 5


# operator  == , > , < , >= , <= , !=
# + - * / **

# a = 5
# b = 7
# print(a < b)

# a = 10
# b = 15
# print(a + b)
#
# print(2 ** 3)

# a = 5
# b = 5
# print(a >= b)
# print(a == b)
# print(a != b)
# print(a < b)


# a = 7
# b = 9
# c = 1
# print(a > b and b < c)
# print(a < b and c > b)
# print(a < b and b > c)

# and , 0=False , 1=True
# 0 and 0 -> 0
# 1 and 0 -> 0
# 0 and 1 -> 0
# 1 and 1 -> 1
# print(a < b and b > c and a > b and b > a)


a = 7
b = 9
c = 1

# print(a > b or c < b)

# or
# 0 or 0 -> 0
# 0 or 1 -> 1
# 1 or 0 -> 1
# 1 or 1 -> 1

# print(a > b or c > b or b > c)
# a = 7
# b = 9
# c = 1
# print(a < b or c > b and a > c)
# print(a < b or c > b and a < b)
# print(a < b and c > b or a < b)
# a = 7
# b = 9
# c = 1
# print(True and False or False)
#
# print(5 + 7 * 3 + 5 / 3 * 10 + 6 - 4)

# ###################################################
# String - نوشتنی یا تکست - رشته - text

# a = 'test'
# b = "hello"
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# a = '123'  # str
# b = 123  # int

# print(a + 19)
#
# c = int(a)
# d = str(b)

# استرینگ ها دنباله ای از کارکترها هستن
# text = 'Hello worldlkjdflkgj dlkjfg kdjfgl;k jfngk jdfngjkn'
#       012345678910   # index
# print(text)
# print(text[0])
# print(text[5])
# print(text[10])
# print(text[11])
# print(len(text))
# print(text[50])
# print(text[-1])
# print(text[-2])
# print(text[-51])

# text = 'Hello worldlkjdflkgj dlkjfg kdjfgl;k jfngk jdfngjkn'
# print(text[4])
# print(text[3:15])  # [start: end]
# print(text[7:30])  # [index: index - 1]


# a = 10
# b = input('یک عدد وارد کنین: ')
#
# c = a + int(b)
# print(c)

text = 'Hello worldlkjdflkgj dlkjfg kdjfgl;k jfngk jdfngjkn'
# print(text[:35])
# print(text[23:])
print(text[::2])  # [start:end:step]
print(text[5:43:3])

