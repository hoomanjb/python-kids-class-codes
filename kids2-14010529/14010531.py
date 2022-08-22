# import random
#
# hads = random.randint(1, 50)
# print('start the game')
# minimum, maximum = 1, 50
#
# while True:
#     user_input = input(f'lotfan yek adad beyn {minimum} ta {maximum} ntekhab konid: ')
#     if user_input.isdecimal():
#         if int(user_input) == hads:
#             print('javab dorost ast.')
#             print(f'javab {hads} hast.')
#             break
#         elif int(user_input) < hads:
#             print(f'adad bishtari ra az {user_input} entekhab kon')
#             minimum = user_input
#         elif int(user_input) > hads:
#             print(f'adad kamtari ra az {user_input} entekhab kon')
#             maximum = user_input
#     else:
#         print('lotfan adad bezar')


# a = [4 ,9 , 10]
# print(min(a))
# print(max(a))

# ##############################################
# import turtle
#
# t = turtle.Turtle()
#
# t.pensize(3)
# t.speed(5)
#
#
# def make_shape(a, b, c):
#     t.color(c)
#     t.begin_fill()
#     for item in range(a):
#         t.fd(50)
#         t.lt(b)
#     t.home()
#     t.end_fill()
#
#
# slide = int(input('shekle morede nazar chand zeli bashad? '))
# angle = int(input('sekle che zavieii dashte bashad? '))
# color = input('che rangi bashe? ')
#
# s = turtle.getscreen()
# make_shape(slide, angle, color)
#
# turtle.mainloop()


# ##################################################
import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

t.pensize(3)
t.speed(0)

# colors = ['red', 'blue', 'yellow', 'green', 'black', 'white', 'orange', 'Salmon', 'Pink']
#
#
# def make_mandala(a):
#     zavie = 360 // a
#     for _ in range(a):
#         # t.pencolor(random.choice(colors))
#         t.pencolor('red')
#         t.circle(100)
#         t.left(zavie)
#
#
# user_input = input('che tedad dayere doos dari? ')
#
# make_mandala(int(user_input))
#
# t.speed(6)
# t.pencolor('blue')
# t.penup()
# t.goto(0, -60)
# t.pendown()
# t.circle(60)
# # t.hideturtle()
# # t.penup()
# # t.goto(300, 0)
# # t.pendown()
# t.home()
t.dot(60, 'blue')
# t.dot(360, 'red')
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()
turtle.mainloop()








