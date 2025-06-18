#9.	User Registration
'''o	Ask for username and password.
o	If username is empty, raise ValueError.
o	If password is less than 6 characters, raise ValueError.
o	Catch and display both errors.'''

try:
    username = input("Ente username : ")
    if username == "":
        raise ValueError("Username cannot be empty.")
    password = input("Enter password : ")
    if len(password) < 6:
        raise ValueError("Password cannot be less than 6 characters.")
    print("Logged in successfully!")
except ValueError as e:
    print("Error : ", e)