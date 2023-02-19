# String , Numbers , List , Boolean - Dict - Tuple - Set
# String (sequence)

# name = 'AniSa'
# print(len(name))
# print(name[1:4])
# print(name[::2])
# print(name[::-1])
# print(type(name))
# print(name.lower())  # lowercase
# print(name.lower())

# a = 'sara'
# b = 'SaRa'
# print(a == b)
# print(a.lower() == b.lower())

# name = 'An-iSa'
# print(name.split(sep='-'))
# upper_name = name.upper()
# print(upper_name)
# print(name)
# a = '@@@-AAA-###-!!! 111'  # sep = جداکننده
# b = a.split(sep='-')
# print(b)

# a = 'te.st@gmail.com'
# print(a.split(sep='@'))

# a = 're                  za'
# b = a.split()
# print(b)
# name = ''
# for item in b:
#     name += item
# print(name)

# a = '         reza          '
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())

# a = 're          za'
# print(a.replace(' ', ''))

# a = 'als@aslkd@alksjd@aks'
# print(a.split(sep='@'))
# print(a.replace('@', '#'))

#
# a = 'asd123asdas'
# if len(a) == 11:
#     for item in a:
#         if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             print('mobile nis!!!')
#             break

# a = '1231231232'
# if len(a) == 11 and a.isdigit():
#     print('ok')
# print(a.isdigit())

# name = 'Asdas'
# print(name.isalpha())
# print(name.isupper())
# print(name.islower())
# print(name.isalnum())
# print(name.istitle())
# print(name.isdigit())


# name = 'Anisa-212311231'
#       0123456789
# print(name.count('a'))
# print(name.count('z'))
# print(name.index('1'))
# print(name.index('z'))  # dastoore khoobi nis
# print(name.find('z'))
# print(name.startswith('+98'))
# print(name.startswith('Anisa-'))


# name = 'Anisa.ir'
# print(name.endswith('.com'))

# ##########################################
# 1. Write a Python program to calculate the length of a string.
# a = 1000
# print(len(a))

# def my_len(text):
#     result = 0
#     if isinstance(text, str):
#         for _ in text:
#             result += 1
#         return result
#     else:
#         return None
# name = 1000
# print(my_len(name))

# #####
# 3. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the empty string.
#
# Sample String : 'w3hhasdasdasdhhw3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : ''

def exam_3(text):
    if len(text) < 2:
        return ''
    else:
        return text[:2] + text[-2:]


a = 'w3asdasdasdw3'
print(exam_3(a))

