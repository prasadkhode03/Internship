#10.	Password Masker
"""Function mask_password(password) returns a masked version
Example: "secret" → "******"
"""

def mask_password(password):
    length = len(password)
    secret = ""
    for i in range (length):
        secret = secret + "*"
    return secret

password = input("Enter your password : ")
print(mask_password(password))

    
