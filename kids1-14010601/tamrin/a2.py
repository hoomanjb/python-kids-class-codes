import turtle

s = turtle.getscreen()
turtle.title('new project')
turtle.bgcolor('white')
t = turtle.Turtle()

t.pensize(7)
t.shapesize(2)
t.speed(1)
t.color('blue')
t.begin_fill()
t.goto(200, 0)
t.goto(200, 200)
t.goto(0, 200)
t.goto(0, 0)
t.end_fill()
t.color('sky blue')
t.begin_fill()
t.goto(-100, 100)
t.goto(0, 200)
t.end_fill()
t.color('green')
t.begin_fill()
t.goto(100, 100)
t.home()
t.end_fill()
t.color('blue')
t.begin_fill()
t.goto(100, 100)
t.goto(200, 0)
t.end_fill()
t.color('brown')
t.begin_fill()
t.goto(100, -100)
t.home()
t.end_fill()
t.color('blue')
t.goto(100, 100)
t.color('white')
t.begin_fill()
t.goto(200, 200)
t.goto(200, 0)
t.goto(100, 100)
t.goto(200, 200)
t.penup()
t.home()
t.end_fill()
t.color('turquoise')
t.begin_fill()
t.goto(200,200)
t.pendown()
t.goto(300, 100)
t.goto(200, 0)
t.goto(200, 200)
t.end_fill()
t.color('gray')
t.begin_fill()
t.goto(100, 300)
t.goto(0, 200)
t.goto(200, 200)
t.end_fill()















turtle.mainloop()
