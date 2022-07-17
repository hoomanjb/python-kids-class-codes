# first_name = 'hooman'

# a = 10

# print(type(a))
# print(type(3.5))
# print(type(3j+9))

# my_number1 = 10
# my_number2 = 25

# operator (عملگر) -> + - * / **
# operand (عملوند)

# s = my_number1 + my_number2
# m = my_number1 - my_number2
# p = my_number1 * my_number2
# d = my_number1 / my_number2
# t = my_number1 ** my_number2 # tavan ->  2 ** 5 = 2 * 2 * 2 * 2 * 2
# g = 26 % 4 # -> baghi mande
# e = my_number1 // my_number2
#
# print(s)
# print(m)
# print(p)
# print(d)
# print(t)
# print(g)
# print(e)
# my_number1 = 10
# print(my_number1)
# my_number1 = my_number1 + 10
# my_number1 += 10
# my_number1 -= 5
# my_number1 *= 2
# my_number1 /= 3
# print(my_number1)

# ################################## #
# Boolean Logic Binary 0 1
# print(True) # 1 2 3  ' ' [1, 2]  {3, 5} {'name': 'hooman} (2 ,4)
# print(False) # 0  ''  []  {, }  {} ()
#
# a = True
# print(type(a))
# print(bool(a))
# a = 1
# print(type(a))
# print(bool(a))
# a = 100000
# print(type(a))
# print(bool(a))
# a = 'salam'
# print(type(a))
# print(bool(a))
#
# b = 0
# print(type(b))
# print(bool(b))
# b = ''
# print(type(b))
# print(bool(b))
# b = False
# print(type(b))
# print(bool(b))
# b = []
# print(type(b))
# print(bool(b))

# operator (عملگر) -> +, - ,* , /  ,**  , < , > , <= ,>=, ==, != ,and ,or ,in ,not in

# a = 5
# b = 5
# print(a < b)
# print(a <= b)
# print(a == b)
# print(a != b)


# olaviat amaliatha -> () ** * / + -

# result = (7 - 5) - 7 / (3 + 10) + 3
# print(result)


# a = 5
# b = 5
# c = 7
# d = 1
# result = a < b and c < d and a < c and d < a
# AND
# 0 0 -> 0   False False -> False
# 0 1 -> 0   False True  -> False
# 1 0 -> 0   True  False -> False
# 1 1 -> 1   True  True  -> True
# print(result)

# result = a < b or c < d or a < c or d < a
# OR
# 0 0 -> 0   False False -> False
# 0 1 -> 1   False True  -> True
# 1 0 -> 1   True  False -> True
# 1 1 -> 1   True  True  -> True
# print(result)


a = 5
b = 5
c = 7
d = 1
result = a < b and c < d or a < c and d < a

#  a < b and c < d :::  (a < b) -> (False and c < d) -> (False and False) -> False
# False :: (False or a < c) -> (False or True) -> True
# (a < b and c < d or a < c):: True -> (True and d < a) -> True and True -> True

result = ((a < b and c < d) or a < c) and d < a

print(result)


