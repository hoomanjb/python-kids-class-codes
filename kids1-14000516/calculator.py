# True 1 5 [1,2 ] ' '
# False 0 [] ''

while True:
    x = input('please select one operator ,if you want to exit type exit or choose(+ , - , * , / , **): ')
    if x == "exit":
        print('bye bye')
        break
    elif x not in ['+', '-', '*', '/', '**']:
        print('wrong choose!')
        continue
    else:
        a = input('please enter first number:  ')
        if a == 'exit':
            print('bye bye')
            break
        b = input('please enter second number:  ')
        if b == 'exit':
            print('bye bye')
            break

    a, b = int(a), int(b)

    if x == "+":
        print(f"result is {a + b} ")
    elif x == "*":
        print(f"result is {a * b} ")
    elif x == "-":
        print(f"result is {a - b} ")
    elif x == "/":
        print(f"result is {a / b} ")
    elif x == "**":
        print(f"result is {a ** b} ")

# ---------------------------------------------------------
def getting_input(text):
    a = input(text)
    if a == 'exit':
        return False
    else:
        return a

def checkin_valid_operators(v):
    if v in ['+', '-', '*', '/', '**', '//']:
        return True
    else:
        return False

def main():
    while 1:
        user_operator = getting_input('please select one operator ,if you want to exit type exit or choose(+ , - , * , / , **): ')
        if not user_operator:
            print('bye bye')
            break
        elif not checkin_valid_operators(user_operator):
            print('wrong input')
            continue
        else:
            adad_aval = getting_input('please enter first number:  ')
            if not adad_aval:
                print('bye bye')
                break
            adad_dovom = getting_input('please enter second number:  ')
            if not adad_dovom:
                print('bye bye')
                break

        adad_aval, adad_dovom = float(adad_aval), float(adad_dovom)

        if user_operator == "+":
            result = adad_aval + adad_dovom
        elif user_operator == "*":
            result = adad_aval * adad_dovom
        elif user_operator == "-":
            result = adad_aval - adad_dovom
        elif user_operator == "/":
            result = adad_aval / adad_dovom
        else:
            result = adad_aval ** adad_dovom

        print("result is {} ".format(result))