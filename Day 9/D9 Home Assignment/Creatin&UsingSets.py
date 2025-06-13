#🔹 Part C: Sets – Creating and Using

'''8.	Create a set s1 = {1, 2, 3, 4, 5}
o	Add the number 6
o	Try adding 3 again. What happens?'''

s1 = {1, 2, 3, 4, 5}
s1.add(6) #Added the number 6
print("List after adding numbers 6 :",s1)
s1.add(3) #Trying to add 3 again
#It does not add the 3 again because set does not allow duplicates

'''9.	Create a set from a list with repeated values:
numbers = [1, 2, 2, 3, 4, 4, 5]
o	Use set() to remove duplicates'''

numbers = [1, 2, 2, 3, 4, 4, 5]
print("\nOriginal List :",numbers)
num_set = set(numbers) #Created a set from a list 
print("Removed Duplicates (list converted into set):",num_set) #Removed the duplicates


#10. Use a loop to print all items in a set.
print("All items of set :", end = " ")
for i in num_set:
    print(i, end = " ")