# user_name = input('user_name: ')
# age = input('age: ')
# shahr = input('shahr: ')
# email = input('email: ')
#
# shahr_ha = ['tehran', 'karaj', 'rasht']
# shahr_flag = False
# if shahr in shahr_ha:
#     shahr_flag = True
#
# email_flag = False
# if '@gmail.com' in email:
#     email_flag = True
#
# message = f"""
# user name is: {user_name}
# age is : {age}
# """
#
# if shahr_flag and email_flag:
#     message += 'hamechi doroste!!!!'
# else:
#     message += 'yechizi kharab ast!!!'
#
# print(message)
a= 10
b='salam'
email = input('email: ')

if '@' in email:
    print('level1')
    if 'gmail' in email:
        print('level2')
        if '.com' in email:
            print('level3')
        else:
            print('not level3')
    else:
        print('not level2')
else:
    print('not level1')

if '@gmail.com' in email:
    print('')



