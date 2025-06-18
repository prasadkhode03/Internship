#Part D: Real-World File Use Tasks
'''10.	Save User Input
o	Ask user for their name and a short bio
o	Save it to a file user_profile.txt
'''

name = input("What is your name? : ")
bio = input("Write about your bio in short. : ")

with open("user_profile.txt", "w") as file:
    file.write(f"Name : {name}")
    file.write(f"\nBio : {bio}")