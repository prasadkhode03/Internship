'''18.	URL Parser
•	Input a URL like "https://www.example.com/home"
•	Extract and print:
o	Domain: example.com
o	Path: /home'''

url = "https://www.youtube.com/watch?v=Ij_m6UhFRLc"

# Remove the protocol
if url.startswith("https://"):
    url = url[8:]
elif url.startswith("http://"):
    url = url[7:]

# Remove 'www.' if present
if url.startswith("www."):
    url = url[4:]

# Split into domain and path
if '/' in url:
    parts = url.split('/', 1)
    domain = parts[0]
    path = '/' + parts[1]
else:
    domain = url
    path = '/'

print("Domain:", domain)
print("Path:", path)

#O/P
'''
Domain: youtube.com
Path: /watch?v=Ij_m6UhFRLc
'''