# a = 10
# b = 15
#
# def func1():
#     global a
#     a += 5
#     c = a + b  # local variable
#     return c
#
# print(a)
# print(b)
# print(func1())
# print(a)

# #################################3

# class Calculator:
#     # class attr
#     made_in = 'China'
#
#     def __init__(self, num1: int, num2: int):     # instance method
#         # instance attr
#         self.num1 = num1
#         self.num2 = num2
#
#     def sum(self):
#         return self.num1 + self.num2
#
#     def div(self):
#         return self.num1 / self.num2
#
#     def prod(self):
#         return self.num1 * self.num2
#
#     def dis(self):
#         return self.num1 - self.num2
#
#     def __repr__(self):
#         return f'This a Calculator Class - made in {self.made_in}'
#
#
#
# cal1 = Calculator(6, 10)
# print(cal1)
# print(cal1.sum())
# print(cal1.prod())
# print(cal1.dis())
# print(cal1.div())


# cal2 = Calculator(9, 5)
# cal3 = Calculator(90, 51)

# pandas

# Object
# first class
# signal
# log
# analyze
# decorator

# def print_func_name(func):
#     def wrapper(*args, **kwargs):
#         print('before func call')
#         func(*args, **kwargs)
#         print('after func call')
#     return wrapper
#
#
# @print_func_name
# def send_sms():
#     print('send Sms To user')
#
#
# @print_func_name
# def send_email(text, email):
#     print(f'send {text} to address email {email}')
#
#
# @print_func_name
# def validate_mobile():
#     print('phone validator')


# validate_mobile()
# send_email(text='salam chetori', email='test@gmail.com')
# send_sms()

# def formatting(lower_case=False):
#     def formatting_decorator(func):
#         def wrapper(text=''):
#             if lower_case:
#                 func(text.lower())
#             else:
#                 func(text.upper())
#         return wrapper
#     return formatting_decorator


# @formatting(lower_case=False)
# def chaape_text(message=''):
#     print(message)


# chaape_text('aksjhdak SFSFa SADASDAS')

class Animal:
    heart = 1
    brain = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def breath(self):
        print('breathing......')

    def sleep(self):
        print('sleep')


class SeaAnimal(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def breath(self):
        print(' Sea Animal Breath ....')

    def swimming(self):
        print('swimming')

class LandAnimal(Animal):

    def breath(self):
        print(' Land Animal Breath ....')

    def walk(self):
        print('walking...')

a = Animal(name='ll', age=55)
print(a.brain)
print(a.sleep)
print(a.breath())

b = SeaAnimal(name='jj', age=15)
print(b.brain)
print(b.breath())