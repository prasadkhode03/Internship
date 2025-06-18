#🔹 Part B: Working with Multiple Errors
'''4.	Math and File Operations Combined
o	Ask user to input a number and a file name.
o	Perform division 100 / number and open the given file.
o	Catch ZeroDivisionError and FileNotFoundError in separate except blocks.'''
try:
    number = int(input("Enter a number : "))
    file_name = input("Enter the file name : ")
    division = 100 / number
    file = open(file_name, "r")
except ZeroDivisionError:
    print("Cannot divide any number by zero.")
except FileNotFoundError:
    print("File does not exists.")


'''5.	Nested Try Blocks
o	In outer try: convert user input to integer.
o	In inner try: divide a fixed number by the input.
o	Catch errors in appropriate places and explain with print statements.'''
try:
    user_input = input("Enter a number : ")
    converted = int(user_input)
    try:
        div = 6000 / number
        print(f"6000 / {number} = {div}")
    except ZeroDivisionError:
        print("Cannot divide 6000 (or any number) by zero.")
except:
    print("Cannot convert str into int.")