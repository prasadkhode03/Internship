'''Part 4: Challenge Task (Real-World API Usage)
Task 6: Fetch Weather Data (OpenWeatherMap API)
1.	Sign up for a free API key at OpenWeatherMap.
2.	Fetch the current weather for a city of your choice.
3.	Print temperature, weather description, and humidity.

Endpoint:
https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'''
import requests

# Step 1: Your API Key (replace this with yours if needed)
api_key = "1e9a435ccaf4b8003e56cb3d97308b41"

# Step 2: Input city name
city = input("Enter the name of city to check its current weather: ")

# Step 3: Build the URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Step 4: Make GET request to the API
response = requests.get(url)
data = response.json()

temperature = data['main']['temp']
description = data['weather'][0]['description']
humidity = data['main']['humidity']

print(f"\nWeather in {city}:")
print(f"Temperature: {temperature}°C")
print(f"Description: {description.title()}")
print(f"Humidity: {humidity}%")
