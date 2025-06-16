#🔹 Part D: Advanced Applications
'''11.	Word Frequency Counter
•	Input a sentence from the user.
•	Count how many times each word occurs using a dictionary.'''

#Sentence = "The manager had to manage the team to manage the project efficiently"
print("Welcome to Word Frequency Counter")
input = input("Enter a sentence : ")
splitted = input.split()
counts = {word : splitted.count(word) for word in splitted}
print("Words with Frequencies : ",counts)





'''14.	Nested Dictionary
•	Create a nested dictionary:
student = {
    	"name": "Ravi",
    	"marks": {
        	"math": 88,
        	"science": 92
    	}
}
•	Access "science" marks from the nested dictionary.'''

'''15.	Dictionary from Two Lists
•	Given:
keys = ["name", "age", "city"]
values = ["Sam", 30, "Delhi"]
•	Combine into a dictionary using a loop or zip().'''

