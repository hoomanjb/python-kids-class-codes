# Regex
# Open file

# abs address
# current

# r - Read
# a - appending
# w - write
# x - create
# t - text
# b - binary



# f = open('download.jpg', 'rb')
# f = open('my_text.txt', 'rt')
# f = open('D:\\Desktop\Folder\my_text.txt', 'rt')  ## windows
# f = open('/Desktop/Folder/my_text.txt', 'rt')  ## linux


# a = f.read()
# print(type(a))

# a = f.read(2)
# print(a)


# b = f.readline()
# c = f.readline()
# d = f.readline()
# print(b)
# print(c)
# print(d)

# print(f.readline(2))


# f = open('my_text.txt', 'rt')
# for item in f:
#     print(item)
# f.close()

# with open('my_text.txt', 'at') as my_file:
#     my_file.write('\nsalam chetori?')

# with open('my_text.txt') as my_file, open('result.txt', 'wt') as res:
#     for line in my_file:
#         if '2' in line or '1' in line:
#             res.write(line)

# #######################################
# REGEX
# REGULAR EXPRESSION
# test@gmail.com

# wild cards
# ^ avale string bahash shoro beshe
# . baadesh harchi bood
# * 0 ya b har tedad
# $ akharae string bayad ba char ghablish tamoom she
# + 1 ya b har tedad
# []  faghad char haii k dar [] hastan ro peyda kon
# {}  b tedadi k migam begard peyda kon

import re
text = 'The spain alksjdalksjdhlaksjdhlakj'
# print(re.search("^The.*spain$", text))
# print(re.search("^The.+spain$", text))
# a = re.search("^The.+spain$", text)
# a = re.search("^The.+spain", text)
# if a:  # TRUE - 1 234 [123]
#     print('peydash kardam!')
# print(a)

# text = 'The spain alksjdalksjdhlaksjdhlakj'
# a = re.findall('12', text)
# print(a)

# text = '123asda45asd123'  # 1a2f3
# a = re.search('[0-9][0-9][0-9]', text)
# print(a)


# print(re.search('ba[artz]q', 'foobarqux'))
# print(re.search('[a-z][a-z]', 'FOOHux'))
# print(re.search('[0-9a-fA-f]', '4'))
# print(re.search('[^0-9]', '412312312312g'))
# print(re.search('hoo.{1,5}n', 'adaqwdahooggfn'))
# print(re.search('^h.*n$', 'hn'))
# print(re.search('^$', ''))

# print(re.search('^[a-zA-Z]{4,10}@gmail\.com$', 'testgmail.com'))
# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# REGEX
