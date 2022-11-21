# class Person:  # Parent, Base, Upper, Father
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def talking(self):
#         print('TALKING........')
#
#
# class Student(Person):  # Second, Child
#
#     # class attr
#     school_name = 'AAA'
#
#     # instance attr
#     def __init__(self, first_name, last_name, class_no=5):
#         super().__init__(first_name, last_name)
#         self.class_no = class_no
#
#     # instance method -> وقتی اسفاده میکنیم که حتما یه آبجکت از کلاس ساخته باشیم و به مقادیر داخل کلاس احتیاج داشته باشیم
#     def talking(self):
#         print(f' {self.first_name} STUDENT TALKING .....')
#
#     # static method -> وقتی استفاده میشه که ما به هیچ چیزی از داخل کلاس احتیاج نداشته باشیم
#     @staticmethod
#     def ringing():
#         print('ringing')
#
#     # class  method -> وقتی استفاده میشه که فقط به ویژگی های اصلی کلاس نیاز داشته باشیم
#     @classmethod
#     def class_method(cls):
#         print(cls.school_name)
#
#
#
# class Teacher(Person):
#     def __init__(self, first_name, last_name, age):
#         super().__init__(first_name, last_name)
#         self.age = age
#
#
#
# person = Person('ali', 'akbari')


# a = input('yechoziiiii')
# class_no = 5
# if a != 5:
#     student1 = Student('reza', 'rezaii', a)
# else:
#     student1 = Student('reza', 'rezaii')
# student1 = Student('reza', 'rezaii')
# print(student1.class_no)
# print(student1.first_name)
# print(student1.talking())
# print(student1.ringing())


# #######################################################
# from datetime import datetime
#
# class Calculator:
#     name = 'casio'
#
#     def __init__(self, no1, no2):
#         self.no1 = no1
#         self.no2 = no2
#
#     def sum(self):
#         return self.no1 + self.no2
#
#     def sub(self):
#         return self.no1 - self.no2
#
#     @classmethod
#     def show_name(cls):
#         return cls.name
#
#     @staticmethod
#     def show_date():
#         return datetime.now()
#
# cal = Calculator(7, 9)
#
# print(cal.sum())
# print(cal.show_name())
# print(cal.sub())
# print(Calculator.show_date())


# #############################################
# lambda

# a = lambda b, c: b * c
#
# print(a(5, 10))
#
# def my_func(n):
#     return lambda a: a * n
#
# x = my_func(6)
# print(x(7))
# print(x(10))
# print(x(3))

# ##################################################
# Error Handling

# print(0/0) # zero-division-error

# print('injaaaaa')

# print(name) # name-error

# Database , connection ,

# print(name)

# Group Ex
# a = 0
# b = 10
# try:
#     print(a / b)
# except ZeroDivisionError as ex:  # alias
#     print('dari bar 0 taghsim mikoni')
#     print(ex)
# except NameError as ex:
#     print('moteghayer tarif nashode')
#     print(ex)
# except Exception as ex:
#     print('other')
#     print(ex)

# try:
#     print(result)
# except Exception as ex:
#     print(ex)

# print('injaaaaaaaaaaa')

try:
    print(name)
except Exception as ex:
    print(ex)
else:  # اگر عملیات موفق باشه اینجا ران میشود
    print('injaaaaaaaaaaaaaa')
finally:  # هر اتفاقی بیوفته در آخر اینجا ران میشود.
    print('finalyyyyyyyyyy')














