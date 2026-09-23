import requests
import json
def trenutna_t(lat,lon):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude" : lat, "longitude" : lon, "current" : "temperature_2m" , "timezone" : "auto" , "forcast_days" : 1}
    call = requests.get(base_url, params = params)
    json = call.json()
    return json["current"]["temperature_2m"]
cities = [
      ("Ljubljna", 46.0511, 14.5051),
      ("Maribor",46.5558, 15.6459),
      ("Celje", 46.2309, 15.2604),
      ("Kranj", 46.2389, 14.3556),
]
for c in cities[:4]:
    print(trenutna_t(c[1],c[2]),c[0])

trenutna_t(45.12,14.5)    

razlika1 = 0
mesto = ""

for c in cities:
    dnevna, nocna = json["current"]["temperature_2m"](c[1], c[2])

    razlika = max(dnevna) - min(nocna)
    if razlika > razlika1:
        razlika1 = razlika
        mesto = c[0]

print()
print("Razlika je:", razlika1, )
print("Mesto:", mesto)