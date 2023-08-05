# error handling
# try - except

# a = input('enter number 1: ')
# b = input('enter number 2: ')
# c = int(a) / int(b)
# print(c)
# TypeError - ValueError - ZeroDivisionError

# a = input('enter number 1: ')
# b = input('enter number 2: ')
# try:
#     c = int(a) / int(b)
#     # session = database --- vasl shodan database : server khamoosh bashe - database nabashe - query eshtebah
# except TypeError as ex1:
#     print(ex1)
#     print('type string ro nemishe taghsim kard')
# except ZeroDivisionError as ex2:
#     print(ex2)
#     print('lotfan adad 0 vared nakonid')
# except ValueError as ex3:
#     print(ex3)
#     print('lotfan faghad adad vared konid!')
# except Exception as ex:
#     print(ex)
#
# print('okkkkk')


# a = input('enter number 1: ')
# b = input('enter number 2: ')
# TypeError - ValueError - ZeroDivisionError
# try:
#     c = int(a) / int(b)  # سعی کن این خط رو انجام بدی
# except Exception as ex:  # اگر خطا به وجود اومد این قسمت اجرا میشه
#     print(ex)
# else:  # اگر خطایی دیده نشد این قسمت اجرا میشه
#     print(c)
# finally:  # چه خطا دریافت شه چه نشه این قسمت همیشه اجرا میشه
#     print('finally')


# try:
#     c = int(a) / int(b)
#     # session begriri database
# except Exception as ex:
#     print(ex)
# else:
#     print(c)
#     # data ro update mikonam
# finally:
#     print('finally')
    # session close kon

# #############################
# Datatype: String - str

name = 'Anisa'
# print(name)
# print(type(name))
# a = 10
# b = str(a)
# name = '123'
# print(name.isdigit())
# name = '1hjh2#3'
# print(name.isalnum())  # alpha numeric
# if name.isalnum() and name.islower():
#     print('ok')
# else:
#     print('nabayad az special chr estefade koni')

# name = 'A1hjh2#3'
# print(name.islower())
# name = 'ASD'
# print(name.isupper())
# name = 'ASD'
# print(name.istitle())
name = 'ⅮⅪ'
print(name.isnumeric())
print(name.isdigit())

