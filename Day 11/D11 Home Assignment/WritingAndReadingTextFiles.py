#🔹 Part A: Writing and Reading Text Files
'''1.	Write a Greeting
o	Create a file called greeting.txt
o	Write "Hello, welcome to Python file handling!" into it.'''

file = open("greeting.txt", "w")
file.write("Hello, welcome to Python file handling!")
file.close()


'''2.	Read File Content
o	Open greeting.txt and print the content.'''
file =open("greeting.txt", "r")
print(file.read())
file.close()


'''3.	Append More Text
o	Append "This is the second line." to greeting.txt
o	Then read and print the updated content.'''
file = open("greeting.txt", "a+")
file.write("This is the second line.")
file.seek(0)
print(file.read())
file.close()