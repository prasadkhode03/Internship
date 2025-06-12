#9.	Email Generator
"""Function generate_email(name, domain="example.com")
•	Input: "John Doe" → Output: "john.doe@example.com" """

def generate_email(name, domain = "example.com"):
    email = name + "@" + domain
    return email

name = input("Enter your name : ")
print("Your email is : ",generate_email(name, "gmail.com"))
