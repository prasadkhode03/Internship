'''15.	Dictionary from Two Lists
•	Given:
keys = ["name", "age", "city"]
values = ["Sam", 30, "Delhi"]
•	Combine into a dictionary using a loop or zip().'''

keys = ["name", "age", "city"]
values = ["Sam", 30, "Delhi"]
person = {}
for i in range(len(keys)):
    person[keys[i]] = values[i]
print(person)