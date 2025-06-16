'''12.	Character Frequency
•	Input a string.
•	Count how many times each character occurs.'''

print("Welcome to Character Frequency Counter")
#string = "Hello I am a very very good boy in the town"
string = input("Enter a string : ")
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Characters with Frequncies - ")
for char, count in char_count.items():
    print(f"{char} : {count}")
