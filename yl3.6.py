#16.10.24 Steven Pikajago
#ülesanne 03.6

import turtle

"""
Ülesanne 3.6: Python Turtle
Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
Loo muutuja kujundi_varv, mis määrab kujundi täitevärvi (string)
Kasutades Turtle'i, joonista kõrvuti värvilised kujundid ruut ja kolmnurk, mis kasutab loodud muutujaid
"""

kylje_pikkus = 100
nurk = 120
kujund_varv = "red"

for i in range(3):
    for i in range (3):
        turtle.forward(kylje_pikkus)
        turtle.left(nurk)


    turtle.penup()
    turtle.forward(kylje_pikkus*1.5)
    turtle.pendown()




turtle.done()
