'''List All Users from JSONPlaceholder
API: https://jsonplaceholder.typicode.com/users
Goal: Display names, emails, and company names of all users.'''
import requests
api = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api)
placeholders = response.json()
for i in placeholders:
    print("Name :", i["name"])
    print("Email :", i["email"])
    print("Company :", i["company"]["name"])
    print("")