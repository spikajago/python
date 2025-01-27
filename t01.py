# 27.01.25 Steven Pikajago
import requests

url = "https://dummy-json.mock.beeceptor.com/roles"

response = requests.get(url)
otsing=input("Otsi rolle ")
if response.status_code == 200:
    data=response.json()
    for valik in data:
        nimi=valik['name']
    print("Viga andmete allalaadimisel:", response.status_code)
          