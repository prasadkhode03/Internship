'''10.	Simple File Reader with Fallback
o	Ask user for a file name.
o	If file doesn’t exist, catch FileNotFoundError and create a new file with default content.
o	Print "New file created."
'''
file_name = input("What is your file name? : ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    default_content = "This is a new file."
    with open(file_name, 'w') as file:
        file.write(default_content)
        print("New file created.")



