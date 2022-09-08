import turtle


s = turtle.getscreen()
turtle.title('کلاس برنامه نویسی 1')
turtle.bgcolor('white')
t = turtle.Turtle()
t.pensize(8)
t.shapesize(2)
t.speed(1)
t.color('red')
t.goto(0,200)
t.begin_fill()
t.color('red')
t.penup()
t.goto(0, 200)
t.pendown()
t.goto(200, 200)
t.goto(200, 0)
t.goto(0, 0)
t.end_fill()
t.goto(100, 0)
t.begin_fill()
t.color('pink')
t.circle(100)
t.end_fill()
t.color('red')
t.penup()
t.goto(0, 0)
t.pendown()

turtle.mainloop()




