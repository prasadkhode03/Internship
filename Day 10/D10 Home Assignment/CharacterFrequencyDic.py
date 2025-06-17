'''12.	Character Frequency Dictionary
•	Input a string and create a dictionary of character counts.
Example: "book" → {'b':1, 'o':2, 'k':1}'''
string = input("What is your string :")          
char_freq = {}
for i in range(len(string)):
    char_freq[string[i]] = string.count(string[i])
print("Character with Frequencies :",char_freq)

