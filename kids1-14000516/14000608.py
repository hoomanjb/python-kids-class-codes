# a = f'{123} {"asda"} {[1,2,3]}'
# b = '{} {} {}'.format(123, "asda", [1,2,3])
# print(a)
# ------------------------------------
# if  <>

# a = "hello world"
# print(a.count('l'))

# def maximum(a, b):
#     if a >= b:
#         print('a is biger than b')
#     else:
#         print('b is biger than a')

# maximum(3, 9)
# maximum(6, 7)
# maximum(34, 9)


# def validate_phone_number(a: str = '091212345678'):
#     if len(a) == 11 and a.isalnum():
#         print('phone number is ok')
#     else:
#         print('phone number is unvalid')
#
# a = '091212345678'
# validate_phone_number()

def sum_two_value(adad1, adad2):
    if isinstance(adad1, str):
        return False
    else:
        result = adad1 + adad2
        return result
    #   return adad1 + adad2

a = sum_two_value(adad1=5 ,adad2=6)
b = sum_two_value(7, a)
print(b)
print(sum_two_value(8 ,b))
print(sum_two_value(adad1='ss', adad2=4))