'''Task:
Get a Random Joke
API: https://official-joke-api.appspot.com/random_joke
Goal: Fetch and display the joke setup and punchline.'''

import requests

url = "https://official-joke-api.appspot.com/random_joke/"
response = requests.get(url)
print("Status Code :", response.status_code)
joke = response.json() #OR  print("Joke : ", response.text)
print("Setup :", joke["setup"]) 
print("Punchline :", joke["punchline"]) 
