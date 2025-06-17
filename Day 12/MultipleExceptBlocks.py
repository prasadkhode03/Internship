'''Multiple Except Blocks
Input: take a number and a file name.
Divide 100 by the number and open the file.
Catch both ZeroDivisionError and FileNotFoundError'''

try:
    number = int(input("Enter a number : "))
    file_name = input("What is your file name? : ")
    
    div = 100 / number
    file = open(file_name, "r")
except ZeroDivisionError:
    print("Cannot divide a number by zero.")
except FileNotFoundError:
    print("File does not exists.")


# except (ZeroDivisionError, FileNotFoundError):
#     print("Exception occur due to wrong input!")

