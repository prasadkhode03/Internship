'''17.	Initials Generator
•	Input: "John Ronald Reuel Tolkien"
•	Output: "J.R.R.T."'''

input = input("What is your name? : ")
words = input.split()

print("Your Initial : ",end = "")
for i in range(len(words)):
    output = words[i][0].upper()
    print(output, end = ".")

#O./P
#What is your name? : Prasad Rajendra Khode
#Your Initial : P.R.K.

