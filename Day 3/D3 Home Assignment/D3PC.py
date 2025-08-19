#Part C: Logical Operators#
"""4.	Create a login check:
o	Ask for username and password
o	If both match predefined values (e.g., "admin" and "1234"), print "Login successful"
o	Else, print "Invalid credentials"
"""
#Asking for username and password
username = input("Enter username : ")
password = input("Enter password : ")
#Matching both predefined values
if(username == "admin" and password == "1234"):
   print("Login successful")
else:
   print("Invalid credentials")


"""5.	Ask the user to enter a number between 100 and 500:
o	Use logical operators to validate the input range."""

num = int(input("Enter a number between 100 and 500 : "))
if(num>=100 and num<=500):
   print("Number is in valid range")
else:
   print("Number is in invalid range")