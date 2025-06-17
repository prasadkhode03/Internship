'''List Access and Conversion
Instructions:
Create a list: data = [10, 20, 30]
Ask the user for an index.
Access that index and convert it to a float.
Catch both IndexError and ValueError.'''

data = [10, 20, 30]
try:
    index = int(input("Enter the index : "))
    value = float(data[index])

# except IndexError:
#     print("List index out of size")
#     print(f"Note : Size of List is {len(data)}")
# except ValueError:
#     print("Invalid Conversion")

except (IndexError, ValueError) as e:
    print("Exception :",e)
else:
    print(f"Value at index {index} is {value}")
