'''Part 2: Making API Requests with Python
Task 3: GET Request (Fetching Data)
Use the JSONPlaceholder API (a free fake API for testing):
•	Endpoint: https://jsonplaceholder.typicode.com/posts
Instructions:
1.	Write a Python script to fetch all posts from the API.
2.	Print the response status code.
3.	Print the first post in the response (JSON format).
Expected Output:
Status Code: 200  
First Post: {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}'''

import requests
api = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api)
posts = response.json()
print(f"All Posts : \n{posts}")
print(f"\nStatus Code :{response.status_code}")
print(f"\nFirst Post : {posts[0]}")
