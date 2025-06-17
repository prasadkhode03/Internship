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


