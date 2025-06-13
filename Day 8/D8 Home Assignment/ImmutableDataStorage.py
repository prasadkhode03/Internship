'''15. Immutable Data Storage
o	Store employee data as:
employee = ("John", "Manager", 55000)
o	Try adding a new field to this tuple. What happens?'''

employee = ("John", "Manager", 55000)
employee[3] = 24 #TypeError: 'tuple' object does not support item assignment
