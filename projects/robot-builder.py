import turtle as t


def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.right(90)
    t.end_fill()
    t.penup()


t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')
# feet
a, b = -100, -150
t.goto(a, b)
rectangle(50, 20, 'blue')
a, b = -30, -150
t.goto(a, b)
rectangle(50, 20, 'blue')
# legs
a, b = -25, -50
t.goto(a, b)
rectangle(15, 100, 'grey')
a, b = -55, -50
t.goto(a, b)
a, b = -15, 100
rectangle(a, b, 'grey')
# body
a, b = -90, 100
t.goto(a, b)
rectangle(100, 150, 'red')
# arms
a, b = -150, -70
t.goto(a, b)
rectangle(60, 15, 'grey')
a, b = -150, 110
t.goto(a, b)
rectangle(15, 40, 'grey')
t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')
# neck
a, b = -50, 120
t.goto(a, b)
rectangle(15, 20, 'grey')
# head
a, b = -85, 170
t.goto(a, b)
rectangle(80, 50, 'red')
# eyes
a, b = -60, 160
t.goto(a, b)
rectangle(30, 10, 'white')
a, b = -55, 155
t.goto(a, b)
rectangle(5, 5, 'black')
a, b = -40, 155
t.goto(a, b)
rectangle(5, 5, 'black')
# mouth
a, b = -65, 135
t.goto(a, b)
rectangle(40, 5, 'black')
t.hideturtle()

