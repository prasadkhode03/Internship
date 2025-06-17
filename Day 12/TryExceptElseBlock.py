'''Ask the user to input a number and a file name.
Divide 100 by the number.
If successful, try to open the given file in read mode.
Use try, except, and else to structure the code.'''

try:
    number = int(input("Enter a number : "))
    file_name = input("What is your file name? : ")
    
    div = 100 / number
    file = open(file_name, "r")
except ZeroDivisionError:
    print("Cannot divide a number by zero.")
except FileNotFoundError:
    print("File does not exists.")

# except (FileNotFoundError, ZeroDivisionError) as e:
#     print("Exception occur due to wrong input! : ", e)
else:
    print("\nDivision :", div)
    print("File Opened Successfully!")
