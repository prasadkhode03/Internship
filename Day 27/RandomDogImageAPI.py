'''Get a Random Dog Image
API: https://dog.ceo/api/breeds/image/random
Goal: Fetch and print the image URL (bonus: open it in the browser with webbrowser.open())'''
import webbrowser
import requests
api = "https://dog.ceo/api/breeds/image/random"
response = requests.get(api)
url = response.json()
msg = url["message"]
print(webbrowser.open(msg))
