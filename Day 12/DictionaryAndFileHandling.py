'''Task 4: Dictionary and File Handling
Instructions:
Create a dictionary: prices = {"apple": 10, "banana": 5}
Ask user for a fruit name and a filename.
Try to print the price of the fruit and open the file.
Catch KeyError and FileNotFoundError.'''

prices = {"apple": 10, "banana": 5}
try:
    fruit = input("Enter a fruit name : ")
    filename = input("Enter a file name : ")
    with open(filename, "r") as file:
        filedata = file.read()
    print(f"\nPrice of {fruit} is {prices[fruit]}")
    print(f"\nData of the {filename} file :\n", filedata)
except KeyError:
    print(f"{fruit} is not available in shop.")
    print(f"Choose from this only - {prices.keys()}")
except FileNotFoundError:
    print(f"Sorry, but the {filename} file does not exists...!")

    

    