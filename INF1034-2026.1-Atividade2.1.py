from turtle import *

t = Turtle()

# Fazendo o plano cartesiano

t.penup()
t.goto(0,-300)
t.pendown()

t.fd(600)
t.stamp()

t.lt(90)

t.penup()
t.goto(-300,0)
t.pendown()

t.fd(600)
t.stamp()

# Fazendo as formas

t.penup()
t.goto(-100,100)
t.pendown()

for _ in range(5):
    t.fd (100)
    t.lt (72)

t.penup()
t.goto(100,100)
t.pendown()

for _ in range(6):
    t.fd (100)
    t.rt (60)

mainloop()
