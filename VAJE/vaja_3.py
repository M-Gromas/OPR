import requests

imena = ["Matic","Nej"]
zlostro = 0
for i in imena:
    stro = requests.get(f"https://agify.io/?name={imena}").json()["stro"]
    if stro > zlostro:
        zlostro = stro
        ime = i
print(ime," Je starejši")
#for i,e in enumerate(imena)
    #print(i,e)
