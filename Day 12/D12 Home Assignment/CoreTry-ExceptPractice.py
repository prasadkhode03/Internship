#🔹 Part A: Core Try-Except Practice
'''1.	Basic Input Validation
o	Ask the user to enter a float number.
o	Catch ValueError and print "Invalid input. Please enter a decimal number." '''
try:
    num = float(input("Enter a float number : "))
except ValueError:
    print("Invalid input. Please enter a decimal number.")

'''2.	String to Integer Conversion
o	Take a string input and try converting it to an integer.
o	Catch exceptions and print the type of error using type(e).'''
string = input("Enter the string : ")
try:
    num = int(string)
except Exception as e:
    print("Excetion :", e)

'''3.	List Index Validation
colors = ["red", "blue", "green"]
o	Ask user to input an index and print the color at that index.
o	Catch IndexError.'''
colors = ["red", "blue", "green"]
try:
    index = int(input("Enter the index : "))
    print(f"Color at index {index} is {colors[index]}.")
except IndexError:
    print("List index out of size")