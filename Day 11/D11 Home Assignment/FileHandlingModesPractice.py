#Part C: File Handling Modes Practice
'''7.	Using 'r' Mode
o	Try to read a file that doesn't exist using 'r'.
o	What error is shown?'''

#file = open("notexists.txt", "r")
#Error - FileNotFoundError: [Errno 2] No such file or directory: 'notexists.txt'

'''8.	Using 'w' Mode
o	Open a file with 'w' mode and write some content.
o	Then open it again with 'r' and print it.
o	Notice: Does previous data persist?'''
with open("file.txt", "w") as file:
    file.write("Hello Sir")
    file.write("Welcome to Python Programming")
    file.write("We are learning File Handling")
    file.write("We are trying to learn modes of File Handling")
    file.close()

with open("file.txt", "r") as file:
    print(file.read())

'''9.	Using 'a' Mode
o	Use 'a' mode to keep adding new lines to a file every time the program runs.'''
with open("file.txt", "a") as file:
    file.write("Welcome!")
    file.write("Good Bye!")
