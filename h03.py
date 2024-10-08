# Steven Pikajago 08.10.24
# IT-24
# 1 rühm
# Harjutus 3

import turtle

"""
Ülesanne 3.1: Tervitus
Loo muutuja nimi, mis sisaldab kasutaja nime (string)
Loo muutuja vanus, mis sisaldab kasutaja vanust (integer)
Loo muutuja keskmine_hinne, mis sisaldab kasutaja keskmist hinnet (float)
Trüki välja lause, mis ühendab kõik kolm muutujat, nt: “Karin, 18 aastat vana ja keskmine hinne on 4.7”
"""
nimi = "üllar"
vanus = 18
keskmine_hinne = 3.5
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))


"""
Ülesanne 3.2: Ostunimekiri
Loo muutuja toode, mis sisaldab toote nime (string)
Loo muutuja kogus, mis näitab, mitu toodet soovitakse osta (integer)
Loo muutuja hind, mis näitab ühe toote hinda (float)
Trüki välja lause, mis ühendab need andmed, nt: “Soovin porgandeid 3, mille tüki hind on 5 eurot.”
"""
toode = "Soovin arbuusi"
kogus = 14 
hind = 6
print(toode+" "+str(kogus)+", mille tüki hind on eurodes "+str(hind))


"""
Ülesanne 3.3: Reisiplaan
Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
Trüki välja lause, mis ühendab need andmed, nt: “Minu reis Soome kestab 5 päeva ja üks öö maksab 30.50 eurot.”
"""



"""
Ülesanne 3.4: Lemmikraamat
Loo muutuja raamatu_pealkiri, mis sisaldab raamatu pealkirja (string)
Loo muutuja lehekylgede_arv, mis näitab raamatu lehekülgede arvu (integer)
Loo muutuja hindamisskoor, mis näitab raamatu hinnet skaalal 1-10 (float)
Trüki välja lause, nt: “Minu lemmikraamat on Sipsik, mis on 16 lehekülge pikk ja mille ma hindan 9.7 punktiga.”
"""



"""
Ülesanne 3.5: Unistuste auto
Loo muutuja auto_mark, mis sisaldab auto marki (string)
Loo muutuja tootmisaasta, mis näitab auto tootmisaastat (integer)
Loo muutuja hind, mis näitab auto hinda (float)
Trüki välja lause, nt: “Minu unistuste auto on Opel aastast 1996, mille hind on 150.90 eurot.”




""
Ülesanne 3.6: Python Turtle
Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
Loo muutuja kujundi_varv, mis määrab kujundi täitevärvi (string)
Kasutades Turtle’i, joonista kõrvuti värvilised kujundid ruut ja kolmnurk, mis kasutab loodud muutujaid
"""
k = 50
varv = "green"



turtle.color(varv)

turtle.fd(k)
turtle.left(90)
turtle.fd(k)
turtle.left(90)
turtle.fd(k)
turtle.left(90)
turtle.fd(k)
turtle.left(90)



turtle.penup()
turtle.goto(k*1.5,0)
turtle.pendown()



turtle.fd(k)
turtle.left(120)
turtle.fd(k)
turtle.left(120)
turtle.fd(k)
turtle.left(120)

turtle.done()
