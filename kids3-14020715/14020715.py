# OOP - Object Oriented Programming
# a = 10
# print(type(a))
# b = int(a)

# class Cat:
#     pass
#
# cat1 = Cat() # object - instance
# cat2 = Cat()
#
# print(cat1)
# print(cat2)

# a = 5
# b = a
# print(id(a))
# print(id(b))


# class Car:
#     # class attribute
#     wheel = 4
#     engine = 1
#
#     # instance attribute
#     def __init__(self, a, b):
#         self.color = color
#         self.model = model
#
#     # instance method
#     def show_engine_counter(self):
#         return self.engine
#
#     def starting(self):
#         print('Starting.....')
#
#     def moving(self):
#         print('Moving.....')
#
#     @classmethod
#     def show_wheel_count(cls):
#         return cls.wheel
#
#     @staticmethod
#     def show_car_company():
#         return 'Company Name'
#
#
#
#
# pride = Car(color='Black', model='Sport')
# benz = Car(color='Gray', model='Auto')

# print(benz.wheel)
# print(pride.wheel)
# print(type(pride))
# benz.starting()
# print(pride.show_engine_counter())

# double undersocre - dunder
# magic method

class Person:

    # def __new__(cls, *args, **kwargs):
    #     print('call __new__')
    #     print(cls)
    #     print(args)
    #     print(kwargs)

    def __init__(self, name):
        self.name = name
        print('call __init__')
        print(self)

    def __repr__(self):
        return 'man ye class az person hastam'


# getter - setter
# attr
# ali = Person()
# reza = Person()
# ali.age = 20
# reza.age = 50
# print(ali.age)
# print(reza.age)

ali = Person( name='ali')
print(ali)
print(ali.name)