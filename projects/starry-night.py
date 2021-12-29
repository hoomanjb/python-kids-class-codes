import turtle as t
from random import randint, random


def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown
    a = (180 / points)
    angle =  a - 180
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
    t.right(angle)
    t.end_fill()


# Main code
t.Screen().bgcolor('white')
while True:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 50)
    ranCol = (random(), random(), random())
    a, b = -350, 300
    ranX = randint(a, b)
    a, b = -250, 250
    ranY = randint(a, b)
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
