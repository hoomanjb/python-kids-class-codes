import turtle

s = turtle.getscreen()
turtle.title("soorat")
turtle.bgcolor("light blue")  # background

t = turtle.Turtle()
t.speed(1)
t.color('blue')
t.pencolor('green')
t.shapesize(3)
t.pensize(4)




t.circle(150)

t.penup()
t.left(90)
t.forward(325)
t.left(90)
t.forward(90)
t.pendown()
t.circle(30)

t.penup()
t.right(180)
t.forward(160)
t.right(90)
t.forward(26)
t.pendown()
t.circle(30)

t.penup()
t.home()





t.left(90)
t.forward(250)
t.right(90)
t.pendown()
t.back(25)
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)

t.penup()
t.home()




t.penup()
t.left(90)
t.forward(50)
t.right(90)
t.pendown()
t.left(60)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

t.hideturtle()





turtle.mainloop()