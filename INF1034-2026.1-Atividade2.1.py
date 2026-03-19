from turtle import *

t = Turtle

# Fazendo o plano cartesiano

penup()
goto(0,-300)
pendown()

t.fd(600)
t.stamp

penup()
goto(-300,0)
pendown()

t.fd(600)
t.stamp

# Fazendo as formas

penup()
goto(-100,100)
pendown()

for _ in range(5):
    t.fd (100)
    t.lt (72)

penup()
goto(100,100)
pendown()

for _ in range(6):
    t.fd (100)
    t.rt (60)

mainloop()