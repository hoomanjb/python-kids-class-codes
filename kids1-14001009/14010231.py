# 2ta adad az man begire

# yeki az gozinehaye zir ra entekhab konid:
# 1- مجموع دو عدد
#2- تفریق دو عدد
# 3- ضربشون
# 4- تقسیمشون
# 0- خدانگهدار


# حلقه loop

# hello = 'hello'
# my_list = [1, 4, 6, 'world', 10]
#
# for item in my_list:
#     my_list.append(0)
#     print(item)


adad_aval = int(input('adad aval ra vared konid: '))
adad_dovom = int(input('adad dovom ra vared konid: '))

temp_list = [1]

for item in temp_list:
    print('yeki az menu haye zir ra entekhab konid: ')
    print('1- amaliate jaam')
    print('2- amaliate zarb')
    print('3- amaliate tafrigh')
    print('4- amaliate taghsim')
    print('0- exit')
    user_choice = input(': ')

    if user_choice == '0':
        print('payan!!!')
    else:
        temp_list.append(0)

        if user_choice == '1':
            print('natijeye amalaite jaam: ')
            print(adad_aval + adad_dovom)
            print('###################')

        elif user_choice == '2':
            print('natijeye amalaite zarb: ')
            print(adad_aval * adad_dovom)
            print('###################')

        elif user_choice == '3':
            print('natijeye amalaite tafrigh: ')
            print(adad_aval - adad_dovom)
            print('###################')

        elif user_choice == '4':
            print('natijeye amalaite taghsim: ')
            print(adad_aval / adad_dovom)
            print('###################')

        else:
            print('lotfan az menu dorost entekhab konid!')
            print('###################')
