from turtle import *

t = Turtle()

# Fazendo o plano cartesiano

t.penup()
t.goto(-300,0)
t.pendown()

t.fd(600)
t.stamp()

t.lt(90)

t.penup()
t.goto(0,-300)
t.pendown()

t.fd(600)
t.stamp()

# Fazendo as formas

t.penup()
t.goto(-100,100)
t.pendown()

t.begin_fill()
t.color("blue")

for _ in range(5):
    t.fd (100)
    t.lt (72)

t.end_fill()

t.penup()
t.goto(100,100)
t.pendown()

t.begin_fill()
t.color("yellow")

for _ in range(6):
    t.fd (100)
    t.rt (60)

t.end_fill()

t.penup()
t.goto(-100,-200)
t.pendown()

t.begin_fill()
t.color("red")

for _ in range (8) :
    t.fd (80)
    t.lt (45)

t.end_fill()

t.penup()
t.goto(300,-200)
t.pendown()

t.begin_fill()
t.color("green")

for _ in range (12) :
    t.fd (60)
    t.lt (30)

t.end_fill()

mainloop()
