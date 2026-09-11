# https://hackmd.io/@lukac/api1
import requests

def trenutna_temp(lat,lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=auto&forecast_days=1"
    call = requests.get(base_url).json()
    print(call["current"]["temperature_2m"])
trenutna_temp(45.12, 14.5)

def trenutna_useskup(lat,lon):
    base_urla = f"https://api.open-meteo.com/v1/forecast?latitude={lon}&longitude={lat}&daily=weather_code,temperature_2m_max,temperature_2m_min&hourly=temperature_2m&start_date=2026-09-04&end_date=2026-09-11"
    call = requests.get(base_urla).json()
    
    print(call["daily"]["temperature_2m_max"])
    print(call["daily"]["temperature_2m_min"])
trenutna_useskup(45.12, 14.5)

