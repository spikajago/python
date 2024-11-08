#16.10.24 Steven Pikajago
#ülesanne 04

"""
#5. Ringi pindala ja Turtle
import turtle

try:
    r=int(input("lisa ringi raadius: "))
    pi=3.14
    s=pi*r**2
    p=2*pi*r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt o {p:.2f} ")
    turtle.circle(r, 360)
    turtle.done()
except:
    print("tegid sisestamisel vea!")
"""
"""
#4. Kingituste pakkimine
try:
    kingitused=int(input("lisa kinkide arv: "))
    maht=5
    pakid=kingitused//maht
    yle=kingitused
    print(f"saad teha {pakid} täis kinkekasti. üle jääb {yle}kingitust")
except:
    print("tegid sisestamisel vea!")
"""
"""
#3. Faili allalaadimine
try:
    failiSuurus=int(input("sisesta faili suurus (MB): "))
    downkiirus=int(input("sisesta allalaadimise kiirus suurus (MB/s): "))
    aeg=failiSuurus/downkiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
except:
    print("tegid sisestamisel vea!")
"""
"""
#2. Raamatute allahindlus
ale=0.3
kogus=3
hind=12.53
summa=hind-(hind*ale)*kogus
print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€ .")
"""

"""
# 1. Aia pikkus
a=int(input ( "sisesta külg 1:"))
b=int(input ( "sisesta külg 2:"))5
p=2*(a+b)
print(f"Aia kogupikkus on {p} meetrit.")
"""

