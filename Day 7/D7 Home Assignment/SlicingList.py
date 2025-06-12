#🔹 Part B: Slicing Lists
"""4.	Given numbers = [10, 20, 30, 40, 50, 60, 70], print:
o	First 3 elements
o	Last 2 elements
o	Elements from index 2 to 5 (excluding 5)
o	Reverse the list using slicing"""

numbers = [10, 20, 30, 40, 50, 60, 70]
print("First three Elements : ", numbers[:3])
print("Last 2 elemnts : ", numbers[-2:]) # or numbers[-1: -3: -1]
print("Elements from index 2 to 5 : ", numbers[2:5])
print("Reverse List : ", numbers[::-1])

"""5.	Create a list alphabets = ["a", "b", "c", "d", "e", "f", "g"]
o	Print every second element using slicing"""
alphabets = ["a", "b", "c", "d", "e", "f", "g"]
print("Second Element : ", alphabets[2:3])

