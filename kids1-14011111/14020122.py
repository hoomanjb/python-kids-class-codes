# 5ta soal az karbar beporsim
# score +1
# esmesham begirim
# har soalam 3bar betoone talash kone
# age dafe aval javab dad 3 daafe baadi 2 daafe baadi 1 age ham k na 0

name = input('enter your name: ')
score = 0
a = 3
for item in range(2):
    answer1 = input('paytakhte iran kojas? 1)Tehran 2)London 3)Shiraz')
    if answer1 == '1':
        print(' Doroste!!! ')
        score += a
        break
    else:
        print('Eshtebah!')
        a -= 1  # a = a - 1


a = 3
for item in range(2):
    answer2 = input('paytakhte iran kojas? 1)Tehran 2)London 3)Shiraz')
    if answer2 == '1':
        print(' Doroste!!! ')
        score += a
        break
    else:
        print('Eshtebah!')
        a -= 1  # a = a - 1

# ############################################
# mashin hesab benevisim
# + - * /
# esme karbaro beporse
# 2ta voroodi begire
# exit

name = input('enter your name: ')

is_true = True
while True:
    while is_true:
        a1 = input('addad avalo begoo: ') #a1 = salam
        for item in a1:
            if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('voroodi eshtebah dobare talash konid!')
                break
            else:
                is_true = False
                break
    is_true = True
    while is_true:
        a2 = input('addad dovom begoo: ')
        for item in a2:
            if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('voroodi eshtebah dobare talash konid!')
                break
            else:
                is_true = False
            break
    operator = input('kodomo mikhay? + - * / exit restart')
    if operator == '+':
        print(int(a1) + int(a2))
    elif operator == '-':
        print(int(a1) - int(a2))
    elif operator == '*':
        print(int(a1) * int(a2))
    elif operator == '/':
        print(int(a1) / int(a2))
    elif operator == 'exit':
        print('BYE,BYE')
        break
    elif operator == 'restart':
        continue
    else:
        print('amalgare eshtebah!')





# C