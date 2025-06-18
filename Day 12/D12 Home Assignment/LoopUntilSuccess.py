'''13.	Loop Until Success
•	Ask the user to enter an integer.
•	If invalid, catch the exception and repeat the question until the input is valid.'''
valid_input = False
while not valid_input:
    try:
        num = int(input("Enter a number: "))
        valid_input = True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"Good, your number is {num}.")      
