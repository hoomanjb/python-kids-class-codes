from turtle import *
import math
import random

title('Isosceles Triangle Circle - PythonTurtle.Academy')
setup(1000, 1000)
setworldcoordinates(-500, -500, 500, 500)
hideturtle()
tracer(0, 0)


# x,y is the center of the base, width: length of base, height: height of triangle from the top to base
# direction:direction from the center of base to top
def IsoscelesTriangle(x, y, width, height, direction, c):
    up()
    goto(x, y)
    seth(direction - 90)
    fd(width / 2)
    p1x, p1y = xcor(), ycor()  # first point: bottom right
    back(width)
    p2x, p2y = xcor(), ycor()  # second point: bottom left
    goto(x, y)
    seth(direction)
    fd(height)
    p3x, p3y = xcor(), ycor()  # third point: top
    goto(p1x, p1y)
    down()
    fillcolor(c)
    begin_fill()
    goto(p2x, p2y)
    goto(p3x, p3y)
    goto(p1x, p1y)
    end_fill()


n = 12
r = 300
width = 2 * r * math.sin(math.radians(180 / n))
height = 200
for i in range(n):
    IsoscelesTriangle(r * math.cos(math.radians(180 / n)) * math.cos(math.radians(i * 360 / n)),
                      r * math.cos(math.radians(180 / n)) * math.sin(math.radians(i * 360 / n)), width, height,
                      i * 360 / n, 'blue')

update()
mainloop()