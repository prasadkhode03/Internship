#🔹 Part A: Tuples – Creating, Accessing, and Use
'''1.	Create a tuple t1 = (10, 20, 30, 40, 50)
o	Print the first and last elements
o	Print elements from index 1 to 3'''
t1 = (10, 20, 30, 40, 50)
print("First Element :", t1[0])
print("Last Element :", t1[-1])
print("\nElements from Index 1 to 3 :", t1[1:4])


'''2.	Create a tuple with mixed data types:
person = ("Alice", 25, 5.4, "Engineer")'''
person = ("Alice", 25, 5.4, "Engineer")
print("\nMixed Data type Tuple :", person)


#3.	Try changing an element in the tuple above and note what error is shown.
# person[1] = 45 #TypeError: 'tuple' object does not support item assignment


#4.	Use a loop to print all elements of t1.
print("\nAll Elements of Tuple t1 -")
for i in range(len(t1)):
    print(f"Element {i+1} : {t1[i]}")


'''5.	Create a tuple with one item only:"
Example: t = ("Python",)
(Why is the comma necessary?)'''
t = ("Python",)

'''The comma is necessary when we are going to create a single element tuple.
If we did not give a comma it will declare it as a str data type (in the given example).'''