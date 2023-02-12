# بازی حدس عدد
# 1 - 50
# بالاتر باید بالای
# پایینتر بیار بالاتر
# حله
# 1 - 50  ->  34
# 40 -> bala tar hads zadi , yekam bia paiin tar
# 1 - 40
# 22 -> paiin gofti bia balatar ,
# 22 - 40
# 30 - 40

# ##############################################
import random  # کتابخونه که یه سری آبجکت رندم درست میکنه

goal = random.randint(0, 50)
start, end = 0, 50
while True:
    try:
        user_input = int(input(f'enter your number ({start}-{end}): '))
    except ValueError as value_error:
        print(f'cherto pert gofti. bayad adad begi, error: {value_error}')
    else:
        if user_input == goal:
            print('wow , you won the game !')
            print('good bye')
            break
        elif user_input > goal:
            print('come down')
            if user_input < end:
                end = user_input
        elif user_input < goal:
            print('come up')
            if user_input > start:
                start = user_input


# #####################################
# try - execpt

# a = input('enter your number 1: ')
# b = input('enter your number 2: ')
# try:
#     c = int(a) / int(b)
# except ZeroDivisionError as zero_error:
#     print(zero_error)
# except ValueError as value_error:
#     print(value_error)
# except Exception as error:
#     print(error)
# else:  # اگر عملیات موفق بود میایم به این قسمت در غیر اینصورت مستقیم میریم به finaly
#     print(c)
# finally:
#     print('harchi shod')

# Exception -> ValueError, ZeroDivisionError
# [parent - child] -- [pedar - farzand]  -- [base - child]



# a = input('enter your number 1: ')
# b = input('enter your number 2: ')
# try:
#     c = int(a) / int(b)
# except Exception as error:
#     print(error)
# else:  # اگر عملیات موفق بود میایم به این قسمت در غیر اینصورت مستقیم میریم به finaly
#     print(c)


class AnisaException(Exception):
    pass