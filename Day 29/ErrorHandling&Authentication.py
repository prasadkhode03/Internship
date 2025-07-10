'''Task 5: Error Handling & Authentication
Instructions:
1.	Try accessing a non-existent endpoint (e.g., https://jsonplaceholder.typicode.com/nonexistent).
2.	Handle the error (check status code, print an error message if request fails).
Example Code:
response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")'''

import requests
url = "https://jsonplaceholder.typicode.com/nonexistent"
response = requests.get(url)

if response.status_code == 200:
    print("Request succeeded!")
    print(response.json())
else:
    print(f"Error: Received status code {response.status_code}")
    print("The requested resource does not exist.")

# try:
#     response = requests.get(url)
#     print(f"Posts :{response.json()}")
# except:
#     print("Failed to create a post. Status Code:", response.status_code)