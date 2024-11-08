#Steven Pikajago IT-24
#tunnikontroll
#15
import turtle

turtle.color('black')
for i in range(4):
    turtle.fd(120)
    turtle.lt(90)

turtle.penup()
turtle.goto(90,0)
turtle.pendown()
turtle.lt(90)
turtle.color('red')
for i in range(3):
    turtle.fd(60)
    turtle.lt(90)
turtle.penup()
turtle.goto(0,120)
turtle.pendown()
turtle.color('black')
for i in range(3):
    turtle.fd(120)
    turtle.lt(120)
    turtle.color('green')
turtle.done()
