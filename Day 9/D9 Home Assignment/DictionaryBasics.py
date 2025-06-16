#🔹 Part A: Dictionary Basics
'''1.	Create a Dictionary
Create a dictionary named student with keys:
o	"name" → "Alice"
o	"age" → 20
o	"course" → "Python"
o	Print the dictionary.'''
student = {"name" : "Alice", "age" : 20, "course" : "Python"}
print("Student : ",student)


'''2.	Access Values
o	Print the value of "name" from the student dictionary.'''
print("\nStudent name : ", student["name"])


'''3.	Modify and Add
o	Change "age" to 21
o	Add a new key "city" with value "Mumbai"'''
student["age"] = 21 #Changing age to 21
student["city"] = "Mumbai" #Adding new key "city" with value "Mumbai"
print("\nStudent after Modification : ",student)


'''4.	Delete Key
o	Remove the "course" key from the dictionary using del.'''
del student["course"]
print("\nDeleted \"course\" key from Student : ",student)


#🔹 Part B: Dictionary Operations
'''5.	Loop Through Dictionary
Write a loop to print each key and its value in the student dictionary.'''
print("\nLooping thorugh dictionary - ")
for key, value in student.items():
    print(f"{key}:{value}")


'''6.	Check Key Existence
o	Use in keyword to check if "name" exists in student.'''
if "name" in student:
    print("\n'name' exists in student.")
else:
    print("\n'name' does not exists in student.")


'''7.	Get with Default
o	Use get() to retrieve "grade" from the dictionary.
Provide default value "Not Assigned".'''
print("\nGrade : ", student.get("grade", "Not Assigned"))