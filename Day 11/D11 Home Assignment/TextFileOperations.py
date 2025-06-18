#🔹 Part B: Text File Operations
'''4.	Write Multiple Lines
o	Create a file bio.txt
o	Write the following lines (each on a new line):
Name: Ravi  
Age: 22  
Course: Python '''
file = open("bio.txt", "w")
file.write("Name: Ravi")
file.write("\nAge: 22")
file.write("\nCourse: Python")
file.close()


'''5.	Read Line by Line
o	Read and print each line from bio.txt using a loop.'''
file = open("bio.txt", "r")
print("Content of bio.txt file - \n")
j = 1
for i in file:
    print(f"Line {j} : {i}")
    j += 1
file.close()


