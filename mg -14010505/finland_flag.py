import turtle

s = turtle.setup(800,500)

t = turtle.Turtle()
t.speed(5)

t.penup()
t.goto(-400, -50)
t.pendown()
#blue cross
t.color("royalblue")

t.begin_fill()
t.goto(400, -50)
t.goto(400, 50)
t.goto(-400, 50)
t.goto(-400, -50)
t.end_fill()


t.penup()
t.goto(-200, -250)
t.pendown()

t.begin_fill()
t.goto(-200, 250)
t.goto(-100, 250)
t.goto(-100, -250)
t.goto(-200, -250)
t.end_fill()

t.hideturtle()

turtle.mainloop()
