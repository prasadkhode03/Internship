'''Weather Reporter
API: https://api.open-meteo.com/v1/forecast
Goal: Input a city’s latitude/longitude → Get current temperature.
If temp > 30°C → print “It’s hot!”
If temp < 15°C → print “It’s cold!”'''
import requests

api = "https://api.open-meteo.com/v1/forecast"

lat = float(input("What is your Latitude? ")) #19.997454 Latitude of Nashik
lon = float(input("What is your Longitude? ")) #73.789803 Longitude of Nashik

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m")

data = response.json()
temperature = data["current"]["temperature_2m"]

print(f"Current Temperature is {temperature}°C.")
if temperature > 30:
    print("It’s hot!")
if temperature < 15:
    print("Its's cold!")
