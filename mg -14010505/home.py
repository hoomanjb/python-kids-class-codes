import turtle

s = turtle.setup(800,500)

t = turtle.Turtle()
t.speed(5)


t.penup()
t.goto(-400, -250)
t.pendown()
t.color("light green")
t.begin_fill()
t.goto(-400, -100)
t.goto(400, -100)
t.goto(400, -250)
t.goto(-400, -250)
t.end_fill()

# make blue sky
t.penup()
t.goto(-400, -100)
t.pendown()
t.color("light blue")
t.begin_fill()
t.goto(-400, 250)
t.goto(400, 250)
t.goto(400, -100)
t.goto(-400, -100)
t.end_fill()

# Sun
t.penup()
t.goto(-300, 100)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()


# House
t.penup()
t.goto(-150, -100)
t.pendown()
t.color("pink")
t.begin_fill()
t.goto(-150, 100)
t.goto(50, 100)
t.goto(50, -100)
t.goto(-150, -100)
t.end_fill()


# tri
t.penup()
t.goto(-150, 100)
t.pendown()
t.color("red")
t.begin_fill()
t.goto(-50, 150)
t.goto(50, 100)
t.end_fill()

# Left Window
t.penup()
t.goto(-130, 50)
t.pendown()
t.color("light blue")
t.pencolor('black')
t.begin_fill()
t.goto(-130, 90)
t.goto(-90, 90)
t.goto(-90, 50)
t.goto(-130, 50)
t.end_fill()
t.goto(-130, 70)
t.goto(-110, 70)
t.goto(-110, 90)
t.goto(-110, 70)
t.goto(-90, 70)
t.goto(-110, 70)
t.goto(-110, 50)


# Right Window
t.penup()
t.goto(30, 50)
t.pendown()
t.color("light blue")
t.pencolor('black')
t.begin_fill()
t.goto(30, 90)
t.goto(-10, 90)
t.goto(-10, 50)
t.goto(30, 50)
t.end_fill()
t.goto(30, 70)
t.goto(10, 70)
t.goto(10, 90)
t.goto(10, 70)
t.goto(-10, 70)
t.goto(10, 70)
t.goto(10, 50)


# Door
t.penup()
t.goto(-120, -100)
t.pendown()
t.color("purple")
t.begin_fill()
t.goto(-120, 0)
t.goto(-50, 0)
t.goto(-50, -100)
t.goto(-120, -100)
t.end_fill()
t.pencolor('red')
t.goto(-120, -50)
t.goto(-110, -50)


# Tree
t.penup()
t.goto(200, -100)
t.pendown()
t.color("brown")
t.begin_fill()
t.goto(200, 0)
t.goto(250, 0)
t.goto(250, -100)
t.goto(200, -100)
t.end_fill()
t.penup()
t.goto(225, 0)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(100)
t.end_fill()


t.hideturtle()
turtle.mainloop()
