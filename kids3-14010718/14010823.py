# 5! = 5 * 4!  -> 5 * 4 * 3 * 2 * 1 = 120
# 4! = 4 * 3!  ->
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 1 -> 1


# def factorial_recursive(a):
#     if a == 1:
#         return 1
#     else:
#         d = a * factorial_recursive(a - 1)
#         return d

# result = factorial_recursive(998)
# print(result)


# n = int (input ())


# def factoriel(adad):
#     facto = 1
#     for i in range(1, 1 + adad):
#         facto = facto * i
#     return facto
#
# print(factoriel(1000000))
# ###########################################################

# class Person:
#     # class attribute
#     nation = 'Iran'
#
#     def __init__(self, first_name, last_name):
#         # instance attribute
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return 'this is a Person object class!!!'
#
#     # instance method
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
# # وراثت inheritance
#
# class Student(Person):
#     pass
#
#
# person1 = Person(first_name='ali', last_name='javadi')
# print(person1)
# print(person1.first_name)
# person1.age = 20
# print(person1.age)
# print(person1.__class__.__name__)
# print(person1.get_full_name())
# person2 = Person(first_name='ali', last_name='javadi')
#
# print(person1 == person2)


class Animal:
    def eating(self):
        return 'animal eating'

    def breathing(self):
        return 'animal breathing'


class SeaAnimal(Animal):
    def eating(self):
        return 'heyvanat daryaii dar ab nafas mikeshan!'

    def breathing(self):
        return 'sea breathing'

    def swimming(self):
        return 'Swimming'


class LandAnimal(Animal):
    def eating(self):
        return 'Land Animal eathing'

    def breathing(self):
        return 'Land Animal breathing'

    def walking(self):
        return 'WALKING...'


class DoZistAnimal(SeaAnimal, LandAnimal):
    pass

# fish = SeaAnimal()
# print(fish.eating())

# lakposht = DoZistAnimal()
# print(lakposht.eating())
# print(lakposht.swimming())
# print(lakposht.walking())
#
# fish = LandAnimal()
# #####################################



class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass




class Person:
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass
