# ماشین حساب بنویسین جمع و ضرب و تفریق و تقسیم 2تا ورودی از کاربر بگیره
# اگر کاربر عدد نداد خطا بهش بده


# a = input('enter first number: ')

# if isinstance(a, int):  # از جنس یا از نوع یا از نوع تایپ
#     a = int(a)
# else:
#     print('WRONG!!!')

# if a.isdigit():  # همش از کارکترهای عدد بود
#     print('ok')
# else:
#     print('WRONG!!!')
#
# b = input('enter second number: ')

# ##########################################
# ماژول یا کتابخانه
# package
# turtle - GUI (graphical user interface)
# پایتون میفهمتش و نیاز به نصب نداره

import turtle

s = turtle.getscreen()
turtle.title('ANISA CLASS GUI')
# turtle.bgcolor('yellow')  # background

t = turtle.Turtle()
t.speed(1)
t.color('blue')
t.pencolor('red')
t.shapesize(3)
t.pensize(3)
# t.forward(100)
# t.back(500)

# t.begin_fill()  # شروع کن به پر کردن یا رنگ کردن
# t.color('green')
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.end_fill()
#
# t.begin_fill()
# t.color('blue')
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.end_fill()

# t.right(90)
# t.right(90)
# t.right(90)
# t.right(90)
# t.right(90)
# t.right(90)
# t.right(90)

# t.begin_fill()
# t.color('green')
# t.forward(50)
# t.right(90)
# t.forward(200)
# t.right(90)
# t.forward(50)
# t.right(90)
#
# t.end_fill()
#
# t.color('white')
# t.right(90)
# t.forward(100)
# t.left(90)
#
# t.begin_fill()
# t.color('red')
# t.forward(200)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(200)
# t.end_fill()


# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

# t.goto(100, 200)

# t.goto(100, 0)
# t.goto(100, 100)
# t.goto(0, 100)
# t.home()


# t.goto(100, 0)
# t.goto(200, 150)
# t.home()

# t.goto(100, 0)
# t.goto(100, -100)
# t.goto(0, -100)
# t.home()
# t.penup()
# t.goto(300, 200)
# t.pendown()
# t.circle(100)

t.dot(100, 'blue')

t.hideturtle()

# loop حلقه
# باز بودن پنجره محیط گرافیکی
turtle.mainloop()








