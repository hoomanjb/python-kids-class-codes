# name = 'hooman-javan-bakht'
# email = 'test@gmail.com'

# print(name.isupper())
# print(name.isdigit())
# print(name.isnumeric())
# print(name.isalpha())
# print(name.isalnum())  # hame 0-9 a-z A-Z
# print(not name.isalnum())  # special char
# a = name.split(sep='-')
# print(a)
# print(name)
# b = name.replace('-', ' ')
# print(b)
# print(name)
# name = name.replace('-', '')
# print(name)
# name = name.upper()
# print(name)

# name.lower()
# name = name.split(sep='-')
# print(name)
# a = '12345'
# b = '@'.join(a)  # iterable
# print(a)
# print(b)

# a = '@@@@@@@@@@h  oo    man         $$$$$$$'
# t = ['@', ' ', '$']
# for item in t:
#     a = a.strip(item)
# print(a)

# t = ['!', '@', '$']
# a = '!!!!!!@@@@@@@@$$$$$$$btebet@@@@@@@!!!!'
# for item in t:
#     a = a.strip(item)
# print(a)
# a = a.lstrip()  # left
# a = a.rstrip()  # right
# print(a)
# n = '!!!!!!!!!!!@@@@@@@@@@egggggggggggggg$$$$$11111'
# print(n.strip("!@g$1"))
# wild cards : \n
# Format String
# a = 'salam'
# b = 'salam2'
# text = '{} asdasdasdasd {}'.format(a, b)
# text2 = f'{a} asdasdasdasd {b}'
# print(text)
# print(text2)
a = 'hooman'
b = 'javan'
c = '123465'
d = 'test@yahoo.com'
# text = '{0} - {1} - {2} - {3} - {0}'.format(a, b, c, d)
text = '{fname} - {lname} - {phone} - {email}'.format(fname=a, lname=b, phone=c, email=d)

print(text)

# text2 = f'{a} - {b} - {c} - {d} - {a}'
# print(text2)

# + = * /
# first name
# last name
#
# salama felani khosh amadi
# 1- jaam
# 2- tafrigh
# 3- zarb
# 4- taghsim
# 5- exit
# :1
# adad1:
# adad2:
# natije: ?

# # 1- jaam
# # 2- tafrigh
# # 3- zarb
# # 4- taghsim
# # 5- exit
# :5
# felani khodafez