'''Task 4: POST Request (Sending Data)
Instructions:
1.	Use the same API to create a new post.
2.	Send a JSON payload with:
{
  "title": "New Post",
  "body": "This is a test post.",
  "userId": 1
}
3.	Print the response (should include the new post with an ID).
Expected Output:
New Post: {'title': 'New Post', 'body': 'This is a test post.', 'userId': 1, 'id': 101}'''
import requests
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
  "title": "New Post",
  "body": "This is a test post.",
  "userId": 1
}
response = requests.post(url, payload)

if response.status_code == 201:
    print("New Post:", response.json())
else:
    print("Failed to create a post. Status Code:", response.status_code)

