
# Parameter
# Argument
# positional argument
# keyword argument

# required argument
# optional argument

# name - type - default - args kwargs -
# def my_func(text: str | int, addad: int = 15, flag=False):
#     return ''+text, flag, addad

# c = my_func('15', 15, True)  # positional argument
# print(c)

# d = my_func(addad=15, text='15', flag=True)  # keyword argument
# e = my_func(text='66')
# print(d)
# print(e)


# def my_func(text: str | int, addad: int = 15, flag=False, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     return ''+text, flag, addad
#
# # a = my_func('15', 20, False, 99, 'test')
# b = my_func(text='salam', test=25, count=30)
# # print(a)
# print(b)

def my_func(addad: int) -> int | bool:
    '''
    :param addad:
    in ye voroodie k bayad addad bashe
    :return:
    '''
    if addad == 0:
        return False
    return addad + 25

a = my_func()
print()