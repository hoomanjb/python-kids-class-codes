from colorama import Fore,Style,Back

print(Fore.GREEN+ 'Hello')
name = input('please enter you name :')
while any(char.isdigit() for char in name):
    print(Fore.RED + 'Error')
    name = input(name + ' please enter your name: ')

last_name = input (''+ name +' please enter last name :')
while any(char.isdigit() for char in last_name):
    print(Fore.RED + 'Error')
    last_name = input(name + ' please enter last name : ')

age = input(''+ name +' '+ last_name +' enter age :')
while any(char.isalpha() for char in age):
    print(Fore.RED + 'Error')
    age = input(''+name +' '+ last_name +'please enter age:')

gmail = input(''+ name +' '+ last_name +' enter address gmail :')

print('welcome '+ name +' '+ last_name +'')
a = print(Fore.WHITE+ 'name : '+ name +'')
b = print('last_name : '+ last_name +'')
c = print('age : '+ age +'')
d = print('gmail : '+ gmail +'')

menu = input(Fore.WHITE+ '>>>>>')
if menu == "edit":
    name = input("Enter new name: ")
    last_name = input("Enter new last name: ")
    age = input("Enter new age: ")
    gmail = input("Enter new gmail: ")
    menu = input(Fore.WHITE+ '>>>>>')
    print(Fore.GREEN + "User information edited successfully!")
elif menu == "exit":
    exit()
elif menu == 'start game':
    def game():
        import random
        options = ['s', 'k', 'g']
        user_score = 0
        ai_score = 0

        while True:
            user_choice = input(Fore.GREEN+ "Choose s, k, g : ")

            if user_choice == "exit":
                break
            elif user_choice not in options:
                print(Fore.RED+ "Invalid choice!")
                continue

            ai_choice = random.choice(options)

            print("Computer chose:", ai_choice)

            if user_choice == ai_choice:
                print("It's a tie!")
            elif user_choice == 's':
                if ai_choice == 'k':
                    print("You lost!")
                    ai_score += 1
                else:
                    print("You won!")
                    user_score += 1
            elif user_choice == 'k':
                if ai_choice == 'g':
                    print("You lost!")
                    ai_score += 1
                else:
                    print("You won!")
                    user_score += 1
            elif user_choice == 'g':
                if ai_choice == 's':
                    print("You lost!")
                    ai_score += 1
                else:
                    print("You won!")
                    user_score += 1

            print("User Score:", user_score)
            print("Computer Score:", ai_score)

            if user_score >= 10 or ai_score >= 10:
                break

        if user_score > ai_score:
            print("You won the game!")
        elif user_score < ai_score:
            print("You lost the game!")
        else:
            print("It's a tie game!")

    game()
else:
    print(Fore.RED + "Invalid menu option!")