# def jaam():
#     a  = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     return a + b
#
#
# def tafrigh():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     return a - b
#
#
# def zarb():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     return a * b
#
#
# def taghsim():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     return a / b
#
#
# if __name__ == "__main__":
#     while True:
#         choice = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")
#
#         if choice == '1':
#             print("The sum is:", jaam())
#
#         elif choice == '2':
#             print("The difference is:", tafrigh())
#
#         elif choice == '3':
#             print("The product is:", zarb())
#
#         elif choice == '4':
#             print("The quotient is:", taghsim())
#
#         elif choice == '5':
#             break
#
#         else:
#             print("Enter correct choice!!")


# import random
#
#
# def get_numbers() -> list:
#     while True:
#         try:
#             first_n = float(input("\nPlease Enter First Number : "))
#             second_n = float(input("\nPlease Enter Second Number : "))
#             return [first_n, second_n]  # {'num1': first_n, 'num2': second_n}
#         except Exception as ex:
#             print(f"\n! Please Enter Number Only !\n your error is: {ex}")
#
#
# def menu() -> str:
#     print("""
# Select One Option
#
# [1] Calculator
# [2] Change Numbers
# [0] Exit
#     """)
#     return input("Select one number : ")
#
#
# def calculate():
#     global numbers  #
#     while True:
#         do = input("\nWhich One [ + , - , / , * ] : ")
#         if do == "+":
#             return numbers[0] + numbers[1]  # numbers.get('num1')
#         elif do == "-":
#             return numbers[0] - numbers[1]
#         elif do == "/":
#             return numbers[0] / numbers[1]
#         elif do == "*":
#             return numbers[0] * numbers[1]
#         else:
#             print("\nPlease Choose From [ + , - , / , * ]\n")
#
#
# print("Hi , Welcome\n")
# numbers = get_numbers()
#
#
# while True:
#     option = menu()
#     if option == "1":
#         print(f"\n Answer is : {calculate()}")
#     elif option == "2":
#         numbers = get_numbers()
#     elif option == "0":
#         options_to_say = ["Good Bye" , "Nice To Meet You" , "Have A Nice Day"]
#         print(random.choice(options_to_say))
#         break
#     else:
#         print('Wrong input')



# try:
#     a = int(input('get number: '))
# except Exception as ex:
#     exit(50)

# exit(5)
# print(10)


# LOG

# import turtle
# turtle.bgcolor('white')
# a = turtle.Turtle()
# a.speed(1)
# a.pencolor('blue')
# for item in range(550):
#     a.forward(item)
#     a.left(91)
#
# turtle.mainloop()

# import colorsys
# import turtle
from turtle import Turtle, Screen
#
# t = Turtle()
# s = Screen()
#
# s.bgcolor('black')
# t.speed(0)
# n= 36
# h = 0
# for i in range(600):
#     c = colorsys.hsv_to_rgb(h,1,0.8)
#     h+=1/n
#     t.color(c)
#     t.left(145)
#     for j in range(5):
#         t.forward(300)
#         t.left(150)


# ################################## #

# print('salam')

# def adder(a: int, b: int) -> int:
#     return a + b

# import calculator

# from calculator import adder, subtract
#
# import calculator as cal
#
# a = 10
# b = 20
#
# f = cal.adder(5, 7)
#
# c = adder(a, b)
# d = subtract(a, b)

# ######################################### #
# import tkinter as tk
# window = tk.Tk()
# test = tk.Label(text='HELLLOOOOOOOOOOOOO')  # Label  # Button  # Entry # Text  # Frame
# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10
# )
# label.pack()
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()
# window.mainloop()


# import tkinter as tk
# import random
#
# colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Brown', 'Purple']
# score = 0
# time_left = 30
#
#
# def start_game(event):
#     if time_left == 30:
#         count_down()
#     ask_color()
#
# def count_down():
#     global time_left
#     if time_left > 1:
#         time_left -= 1
#         time_lable.config(text=f'Time left: {time_left}')
#         time_lable.after(1000, count_down)
#
# def ask_color():
#     global score
#     global time_left
#     if time_left > 1:
#         user_input.focus_set()
#         if user_input.get().lower() == colors[1].lower():
#             score += 1
#         user_input.delete(0, tk.END)
#         random.shuffle(colors)
#         lable.config(text=str(colors[0]), fg=str(colors[1]))
#         score_lable.config(text = f'Score: {score}')
#
# window = tk.Tk()
# window.title('COLOR GAME')
# window.geometry('450x220')
# quide = tk.Label(window, text='Insert color in the box not word text...', font=('arial', 15))
# quide.pack()
#
# score_lable = tk.Label(window, text='press enter to start', font=('arial', 15))
# score_lable.pack()
#
# time_lable = tk.Label(window, text=f'time left: {time_left}', font=('arial', 15))
# time_lable.pack()
#
# lable = tk.Label(window, font=('arial', 15))
# lable.pack()
#
# user_input = tk.Entry(window)
# window.bind('<Return>', start_game)
# user_input.pack()
# user_input.focus_set()
# window.mainloop()

