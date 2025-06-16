# file = open("notes.txt", "w") .

# file.write("File Handling Example...") #Writing the content in file
# file.write("Hello World!!!") 

# print(file.tell()) #To check the pointer position
# file.seek(0) #Used to set the pointer position as require

# # print(file.read())

# file.close()

with open("notes.txt", "w+") as file: #No need to close the file
    
    file.write("File Handling Example...") #Writing the content in file
    file.write("Hello World!!!\n")
    file.write("I am Diploma Student\n")
    file.write("Learning Computer Engineering\n")
    file.write("""Trying to learn python
    programming with ai and automation
    ok byee goodd""")
    # print(file.tell())
    # print(file.readline()) #Read first line only
    # print(file.readlines())  #Read all lines as list element of each
    file.seek(0)
    count = 0
    for i in file:
        count+=1

    print("Total number of lines : ",count) #Total number of lines

    file.seek(0)
    result = file.read()
    demo_list = result.split()

    print("Total number of word in the file : ",len(demo_list)) #Total number of word in the file
    # OR print("Total number of word in the file : ",len(result.split()))

    print("Total number of character in the file : ",len(result)) #Total number of character in the file
    

