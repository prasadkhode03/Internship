'''16.	Set-Based Filtering
o	Ask user to enter 5 numbers (some duplicates allowed)
o	Store them in a list
o	Use a set to display only unique numbers'''

num_list = []
print("Enter 5 numbers (some duplicates allowed) -")
for i in range(5):
    num = int(input(f"Enter Number {i + 1} :"))
    num_list.append(num)
print("Orginal List :",num_list)
print("List after converting in Set (Unique numbers): ",set(num_list))