# 29. Write a Python program to set the indentation of the first line.
# 25. Write a Python program to create a Caesar encryption.  a b c -> x y z

# ##########################################################
# format string = 2model ( ''.format()  -  f'' )
name = 'Anisa'
age = 20
# text = '{name} be web site khosh amadid. sene shoma {age}'
# print(text.format(name=name, age=age))
# print(f'{name} be web site khosh amadid. sene shoma {age}')

# format string options: {name:[[fill]align][sign][#][0][width][,][.precision][type]}
# text = '{name:10.10} be web site khosh amadid. sene shoma {age}'
# text = '{name:>10} be web site khosh amadid. sene shoma {age}'
# text = '{name:#^10} be web site khosh amadid. sene shoma {age}'  # {} curve bracket - [] squre bracket
# print(text.format(name=name, age=age))

# a = '{:d}'.format(50)  # decimal - addad sahih - integer
# a = '{:f}'.format(3.1432165498)  # float
# a = '{:.2f}'.format(12323.1432165498)
# a = '{:5.2f}'.format(12.1432165498)
# a = '{:05.2f}'.format(3.143216549)
# a = '{:010.2f}'.format(3.143216549)
# print(a)

# fill = '@'
# align = '^'
# width = 15

# {name:[[fill]align][sign][#][0][width][,][.precision][type]}
# name, age = 'anisa', 30
# text = f'{name:{fill}{align}{width}} b web site ma khosh amadid sene shoma'

# ############################################## #
# ordered, changeable , allow duplicate value
# my_list = [1, 3, 5, 'hello', [7, 8], 'world', [99, 0, [23, 70, 'ok']], 'hello']
# print(type(my_list))
# print(my_list[0])
# print(my_list[6][2][0])
# print(my_list[6][2][2][0])
# print(my_list[6][2][2])
# print(my_list[-1])
# print(my_list[-1][::-1])

# my_list = ['ok', 3, 5, 'hello', [7, 8, 5], 'world', [99, 0, [23, 70, 'ok']], 'hello']
# print(my_list.count(5))
# print(my_list.count('hello'))
# print(my_list.index([7, 8, 5]))
# print(my_list.index([7, 8, 5]))
# print(my_list.index(3))
# print(my_list.index(999))
# print(my_list[0])
# print(my_list.index('ok'))

# print(my_list.index('world'))
# print(my_list.index(7))

# a = [6, 2, 4, 6, 7, 1]
# print(a)
# a.sort(reverse=True)
# print(a)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana", 10]
# thislist.sort()
# print(thislist)

# a = [6, 2, 4, 6, 7, 1]
# a.pop()
# print(a)
# a.pop(2)  # shomare index
# print(a)
# a.remove(6)  # value
# print(a)

# a = [6, 2, 4, 6, 7, 1]
# a.append(9)
# print(a)
# a.append([10, 11])
# print(a)
# a.insert(0, 'hello')
# print(a)
# a.insert(2, [99, 100])
# print(a)

# a = [1, 2]
# b = [1, 2]
# print(a == b)
# print(id(a))
# print(id(b))

# a = [1, 2]
# b = a.copy()
# print(a == b)
# print(id(a))
# print(id(b))
# a.append(10)
# print(a)
# print(b)

# deep copy va shadow copy
