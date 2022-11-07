# OOP - Object Oriented Programming


# a = 'salam'
# print(type(a))
# print(a.split())

# #################################### #
# attribute = vijegi
# class Human:
#     # class attribute -> ویژگی های ثابت در هر کلاس
#     pa = 2
#     dast = 2
#     cheshm = 2
#     kale = 1
#     bini = 1
#     goosh = 2
#
#     def __init__(self, ghad):  # initialize = در ابتدا بوجد آمده
#         self.ghad = ghad
#
#     def chanta_pa_dare(self):
#         return pa
#
#
# akbar = Human()  # variable - instance - object
# print(akbar.pa)
# asghar = Human()
# print(asghar.pa)

# CamelCase
# class Car:
#     # class attr
#     charkh = 4
#     motor = 1
#     ayne = 2
#
#     def __init__(self, sorat, gheymat, rang):  # magic method: __init__
#         # instance attr
#         self.sorat = sorat
#         self.gheymat = gheymat
#         self.rang = rang
#
#     # instance method
#     def get_sorat(self):
#         return f'sorate mashine shoma barabare: {self.sorat}'
#
#     def harekat_kardan(self):
#         return 'mashin dar hale harekat ast.'
#
#
#
# pride = Car(sorat=100, gheymat=200, rang='abi')
# benz = Car(sorat=200, gheymat=500, rang='meshki')
# peykan = Car(sorat=200, gheymat=100, rang='zard')
#
# print(pride.motor)
# print(benz.motor)
#
# print(pride.gheymat)
# print(benz.gheymat)
#
# print(pride.get_sorat())
# print(benz.get_sorat())
#
# pride.sorat = 900
# print(pride.get_sorat())
# pride.boogh = 1
# print(pride.boogh)
#
# print(pride.harekat_kardan())
#
# a = 'salam'
# print('salam'.upper())

# ########################################
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# p1 = Person(first_name='hooman', last_name='javanbakht', age=30)
# print(p1.first_name)
# print(p1.get_full_name())
#
# p2 = Person(first_name='ali', last_name='akbari', age=5)
# print(p2.get_full_name())

# class Calculator:
#     def __init__(self, addad1, addad2):
#         self.addad1 = addad1
#         self.addad2 = addad2
#
#     def sum(self):
#         return self.addad1 + self.addad2
#
#     def prod(self):
#         return self.addad1 * self.addad2
#
#     def sub(self):
#         return self.addad1 - self.addad2
#
#     def divide(self):
#         return self.addad1 / self.addad2
#
# c1 = Calculator(5, 6)
# c2 = Calculator(9, 15)
#
# print(c1.prod())
# print(c2.divide())

# a = 10
# a = 20
# a = 30
#
# match a:
#     case 10:
#         print('a == 10')
#     case 20:
#         print('a == 20')
#     case 30:
#         print('a == 30')
#     case _:
#         print('yechizi')
#
# if a == 10:
#     print('a == 10')
# elif a == 20:
#     print('a == 20')
# elif a == 30:
#     print('a == 30')
# else:
#     print('yechizi')

# ############################################ #
# class Person:
#     def __init__(self, first_name=None, last_name=None):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     # def set_first_name(self):
#     #     self.first_name = input('enter your first_name: ')
#     #
#     # def set_last_name(self):
#     #     self.last_name = input('enter your last_name: ')
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# p1 = Person()
# print(p1.get_full_name())
# p1.first_name = 'hooman'
# p1.first_name = input('ssss: ')
# p1.last_name = input('ssss: ')
# print(p1.get_full_name())
# print(p1.first_name)

# ################################### #

# class - 2ta addad - 4ta amal asli mashin hesab ro dashte bashe
# 5, 7   5*1 ta 5*10   - 7*1 ta 7*10
# masahat - mohit -
# ezafi: turtle : mostatil

