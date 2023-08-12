# deep copy  shallow copy

# format String
# name = 'Anisa'
# text = f'my name is {name}'
# text2 = 'my name is {name}'.format(name=name)

# age = 12
# name = 'Anisa'
# text = f'my name is {name:>10} and my age is {age}'
# text = f'my name is {name:^.10} and my age is {age}'
# text = f'my name is {name:#^10} and my age is {age}'
# text = f'my name is {name:^.10} and my age is {age}'
# 3.465468984656845
#
# align = < > ^
# {name:[[fill]align][sign][#][0][width][,][.precision][type]}

# print(text)

# a = '{:d}'.format(3)  # adad sahih
# a = '{:3.2f}'.format(5454566.45654654654654654)
# print(a)
# search konid bara 2shanbe

# name = 'asnisaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# print()


# ##############################33
# name = 'anisa'
# align = '<'
# a = f'{name:align}'

# ########################## #
# Tuple - ordered - duplicate - unchangble

# a = (3, 5, 7, ['salam'], True)
# print(a)
# print(type(a))
#
# b = [4, 6, 8, 1]
# c = tuple(b)

# a = (5, 7)
# b = list(a)
# b[0] = 99
# a = tuple(b)
# print(a)


my_tuple = (5, 7, 8, 2, 'salam')
# print(my_tuple)
# # my_tuple[0] = 5
# print(my_tuple.count(5))
# print(my_tuple.index('ok'))
# print(tuple)
# immutable and mutable sequence

# for item in my_tuple:
#     print(item)
# a, b, *c = 5, 9, 10, 99, 55, 99
# print(c)

# #####################################
# set - unordered , unchangble , unduplicate
a = {4, 6, 8, 22, 'salam', 66, 4, 4}
# print(a[0])
# print(a)

# b = [5, 7, 8, 8, 8, 6, 2, 3, 3]
# print(list(set(b)))

a = {4, 6, 8, 22, 'salam', 77, 4, 4, 2}
b = {1, 2, 3, 4}
# print(a)
# print(b)
# print(a.pop())
# a.remove(4)
# a.add('ok')
a = {4, 6, 8, 22, 'salam', 77, 4, 4, 2}
b = {1, 2, 3, 4, 'ok'}
c = a.union(b)  # اجتماع
d = a.difference(b)
e = b.difference(a)
# a.difference_update(b)
# print(d)
# print(e)
# print(a)
f = a.intersection(b)
g = a.symmetric_difference(b)
print(g)
a.issuperset()