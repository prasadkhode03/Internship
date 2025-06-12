#🔹 Part C: Modifying Elements

#6.	Replace the third element of a list marks = [45, 67, 89, 34] with 99.
marks = [45, 67, 89, 34]
print("List before Replacing Element :", marks)
marks[3] = 99
print("List after Replacing Element :", marks)


#7.	Add an element "python" at the end of a list languages = ["C", "Java"].
languages = ["C", "Java"]
print("\nList before appending element :",languages)
languages.append("Python")
print("List after appending element :",languages)


#8.	Insert "HTML" at index 1 in the above list.
languages.insert(1, "HTML")
print("\nList after Inserting \"HTML\" element :", languages)


#9.	Remove the last item using pop() and print it.
popped = languages.pop()
print("\nPopped element :",popped)
print("List after popping element :",languages)


#10. Delete the second element using del.
del languages[2]
print("\nList after deleting 2nd element :",languages)