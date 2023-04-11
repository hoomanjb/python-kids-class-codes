UserName = input('Enter Your Name')

point = 0

for item in range(2):
    Soal1 = input('2*5??')
    if Soal1 == '10':
        print("gozine dorost ast")
        point += 1
        break
    else:
        print('eshtebah')

for item2 in range(2):
    soal2 = input('paytakhte Iran Kojast?? 1)tehran 2)Tabriz 3)Mozandaran')
    if soal2 == '1':
        print('dorost ast')
        point +=1
        break
    else:
        print('eshtebah ast')

print('emtizate shoma')
print(point)
print('your name:')
print(UserName)
