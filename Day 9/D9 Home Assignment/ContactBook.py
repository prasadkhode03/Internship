#🔹 Part C: Real-World Dictionary Use Cases
'''8.	Contact Book
o	Create a dictionary contacts with 3 people’s names as keys and their phone numbers as values.
o	Add a new contact.
o	Update one contact’s number.
o	Delete one contact.'''
contacts = {"Om" : 9921390180, "Rutvik" : 7620007358, "Atharva" : 7030036662}
print("Contacts : ", contacts)

contacts["Satvik"] = 9423575365 #Added a new contact
print("Contacts after adding a new contact : ", contacts)

contacts["Om"] = 9923520356 #Updated one contact's number
print("Contacts after updating one contact's number : ", contacts)

del contacts["Rutvik"] #Deleting one contact number
print("Contacts after deleting one contact's number : ", contacts)


