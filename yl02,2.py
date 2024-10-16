# Steven Pikajago 08.10.24
# IT-24
# Sinilill


import turtle
aken = turtle.Screen() 
aken.setup(width=500, height=500)
aken.title("Sinilill Steven Pikajago")
turtle.speed("fastest")
turtle.pensize(10)


turtle.pencolor("green")
turtle.left(90)
turtle.fd(-150)
turtle.fd(200)


turtle.begin_fill()
turtle.color("blue", "lightblue")
turtle.pencolor("blue")
turtle.right(90)
turtle.circle(60)
turtle.end_fill()


turtle.left(90)
turtle.penup()
turtle.fd(40)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow", "yellow")
turtle.right(90)
turtle.circle(20)
turtle.end_fill()



turtle.begin_fill()
turtle.color("green", "green")
turtle.penup()
turtle.goto(-10,-50)
turtle.pendown()
turtle.pencolor("green")
turtle.left(90)
turtle.fd(50)
turtle.left(120)
turtle.fd(50)
turtle.left(120)
turtle.fd(50)
turtle.left(120)
turtle.end_fill()



turtle.done()