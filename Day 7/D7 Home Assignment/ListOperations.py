'''16.	Write a program that takes 5 numbers from the user and stores them in a list. Then:
•	Print the sum
•	Print the max and min number
•	Sort the list and print it'''

my_list = []
for i in range(5):
    my_list.append(int(input(f"Enter Number {i+1} : ")))

sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
print("\nSum =",sum)

max = 0
for i in range(len(my_list)):
    if my_list[i] > max:
        max = my_list[i]
print("Max =", max)

min = my_list[i]
for i in range(len(my_list)):
    if my_list[i] < min:
        min = my_list[i]
print("Min =", min)
my_list.sort()
print("Sorted List :", my_list )


'''17.	Create a list names = ["Alice", "Bob", "Charlie", "David"]
•	Use list comprehension to create a list of name lengths: [5, 3, 7, 5]'''
names = ["Alice", "Bob", "Charlie", "David"]
lengths = [len(name) for name in names]
print("List of name lengths :",lengths)

#18.	Given sentence = "Python is powerful", convert it into a list of words and then reverse the list using slicing.
sentence = "Python is powerful"
words = sentence.split()
print("List of words :", words)
words.reverse()
print("Reversed List :", words)