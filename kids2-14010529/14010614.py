# import random
# # ramz bayad misakhtim
#
# # name_list = ['apple', 'book', 'car', 'havij', 'hooman']
# spec_char = ['!', '@', '~', '#', '?', '%', '&']
# lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'l', 'o', 't']
# upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'L', 'O', 'T']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# while True:
#     char_len = int(input('che tedad password char niaz darid: '))
#
#     which_letter_case = input('az horoof koochik estefade beshe ya bozorg ya hardo? 1-lower 2-upper 3-both : ')
#
#     want_number = input('adad dar password estefade shavad? 1-yes 2-no : ')
#
#     want_special = input('az special char estefade shavad? 1-yes 2-no : ')
#
#     random_choice = []
#
#     if which_letter_case == '1':
#         random_choice.extend(lower_case)
#     elif which_letter_case == '2':
#         random_choice.extend(upper_case)
#     elif which_letter_case == '3':
#         random_choice.extend(lower_case)
#         random_choice.extend(upper_case)
#     else:
#         print('shoma az horof estefade nakardid!')
#
#     if want_number == '1':
#         random_choice.extend(numbers)
#     else:
#         print('shoma az addad estefade nakardid!')
#
#     if want_special == '1':
#         random_choice.extend(spec_char)
#     else:
#         print('shoma az special char estefade nakardid!')
#
#     password = ''
#     for item in range(char_len):
#         password += random.choice(random_choice)
#     print(password)
#     print()
#     a = input('agar mikhay edame bedi? 1-yes 2-exit : ')
#     if a == '1':
#         continue
#     else:
#         print('byby')
#         break
#
# import string
# import random
#
# ## characters to generate password from
# characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
#
# def generate_random_password():
#     ## length of password from the user
#     length = int(input("Enter password length: "))
#
#     ## shuffling the characters
#     random.shuffle(characters)
#
#     ## picking random characters from the list
#     password = []
#     for i in range(length):
#         password.append(random.choice(characters))
#
#     ## shuffling the resultant password
#     random.shuffle(password)
#
#     ## converting the list to string
#     ## printing the list
#     print("".join(password))
#
#
# ## invoking the function
# generate_random_password()

# ############################################
# List => order - tekrari - avaz konim  - a =  [1, 2, 3, 3, 3] -  a[1] = 10
# Tuple => order - tekrari - avaz nemishe -
# b = [(1, 2), (5, 6)]
# a = (3, 5, 6, 9, 'hello', [4, 5], (7, 9), True)
# print(type(a))
# print(a[0])
# print(a[-1])
# a[0] = 5  # Wrong
# c = list(a)
# print(c)
# c[1] = 10
# a = tuple(c)
# print(a)

# a = (3, 5, 6, 9, 'hello', [4, 5], (7, 9), True)
# print(a.index(3))
# print(a.count(3))

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# v = (a, b, c, *d) = fruits
# print(v)
# print(b)
# print(c)
# print(d)

# b = 5
# a = 5
# c = 5
# d = 5
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# a = 10
# print(id(a))
# fruits = (("apple", "banana"), ("cherry", "strawberry"), ("raspberry", 'a'))
# for item1, item2 in fruits:
#     print(item1, item2)






