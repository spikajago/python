# 22.10.24 Steven Pikajago
# ülesanded 7 loendid

"""
# Jukebox
muusika=['ALIKA – "Bridges"',
'Anett x Fredi – "Read Between The Lines"',
'villemdrillem – "leekiv armastus"',
'Clicherik & Mäx – "PAKSUD"',
'nublu – "ära ärata"',
'NOËP – "Move Your Feet"',
'Trad.Attack! – "Bring It On"',
'Bedwetters – "It Is What It Is"',
'Reket – "Panama paberid"',
'Grete Paia – "Võluväel"']

for i in range(len(muusika)):
    print(str(i+1)+". "+muusika[i])
try:
    valik=int(input("vali laul: "))
    print(f"Mängin lugu {muusika[valik-1]}")
except:
    print("Midagiläks katki. Teavita adminni")
"""

import datetime
x=datetime.datetime.now()
tana=int(x.strftime("%m"))-1 

#12 kuud

kuud=[["jaanuar",-15,-6,-1,21,-1,18,-2,10,-18,-3,-10,29,10,24,30,13,-11,17,12,-4,-18,-19,25,-11,-17,8,6,28,-15,3,179],
["veebruar",22,10,21,27,12,-5,-15,-1,18,14,8,30,20,2,9,17,17,0,9,1,22,-7,27,-12,14,3,24,27],
["märts",21,26,23,5,18,-3,-4,3,0,22,16,-7,26,-12,-17,4,-20,16,-2,-4,5,8,-10,-13,22,-8,-18,22,3,1,20],
["aprill",14,4,10,16,9,18,18,-1,26,-12,25,4,13,9,-3,24,-14,-2,24,-18,-2,-9,-2,-13,0,4,24,-6,9,-14],
["mai",-14,27,8,5,23,-7,16,15,25,-14,0,8,24,30,9,9,-13,-20,-2,8,-20,8,25,-13,28,-3,1,-5,21,23,6],
["juuni",-1,29,-14,30,28,1,9,-7,20,26,-19,26,-9,0,6,28,-2,13,8,28,14,-20,2,7,-9,24,-13,0,9,-11],
["juuli",-14,-20,-16,6,30,-11,24,-15,25,-13,-1,10,3,-11,-2,4,16,-18,-10,20,29,22,10,6,1,15,15,-13,15,-7,-12],
["august",-4,22,27,4,19,-8,-17,-15,-7,23,1,-14,27,16,8,23,-5,-7,-20,-2,22,-16,29,28,6,23,0,12,-14,27,-20],
["september",0,29,30,2,27,4,5,15,13,23,20,-18,-16,6,-7,24,7,-18,28,25,-6,30,18,-8,3,-10,-11,10,-13,-10],
["oktoober",16,-13,30,5,-12,21,24,-6,14,29,-17,-5,29,-10,-15,-5,-6,14,-4,-20,9,26,0,-2,-17,29,7,-5,29,18,10],
["november",-11,-14,9,-16,25,-20,-2,-16,24,-14,-12,21,-2,-6,29,-12,-4,-18,11,15,24,-13,-16,25,-15,-14,-10,26,27,25],
["detsember",24,-13,-2,15,-16,18,7,7,19,-18,-17,-11,1,27,-10,21,26,-2,18,-9,27,8,-12,-8,-17,26,15,-20,-14,-9,-3]]

#ülesanded
print(kuud[tana])
print(f"viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine=[]
for i in range(len(kuud[tana])-1):
    ajutine.append(kuud[tana][i+1])
    print(kuud[tana][i+1], end=", ")

print()
print(f"Max temp: {max(ajutine)}")
print(f"min temp: {min(ajutine)}")
print(f"keskmine temp: {sum(ajutine)/len(ajutine)}")

print(f"-20 esineb {ajutine.count(-20)} korda")
ajutine.pop(5)
print(ajutine)

