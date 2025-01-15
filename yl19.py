# 14.01.25 Steven Pikajago
# ülesanded 19
import json
kl12=0
kl11=0
kl10=0
with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    opilased = json.load(file)

    
    for opilane in opilased:
        if opilane["klass"]=="12":
            kl12+=1
            print(opilane['nimi'])
            for trenn in opilane ["tegevused"]:
                print(trenn)
            for aine, punktid in opilane["hinded"].items():
                print(aine, punktid)
            print("---------------------")




print(f"12. klassis õpib {kl12} õpilast")