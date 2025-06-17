# Part A: Indexing & Slicing
'''1.	Basic Indexing
Given: text = "PythonProgramming"
o	Print the first, fifth, and last character using indexing.'''

text = "PythonProgramming"
print("Text : ", text)
print("First Character : ", text[1])
print("Fifth Character : ", text[5])
print("Last Character : ", text[-1])


'''2.	Basic Slicing
From the same string:
o	Print the substring "Python"
o	Print the substring "Programming"
o	Print every second character (::2)
o	Reverse the string using slicing'''

print("\nSubstring \"Python\" : ",text[:6])
print("Substring \"Programming\" : ",text[6:])
print("Every second character : ",text[::2])
print("Reverse string : ", text[::-1])


'''3.	Custom Substring
Input a string from the user and print:
o	First 3 characters
o	Last 3 characters
o	Middle 5 characters'''

string = input("Enter the string : ")
print("First 3 characters : ",string[:3])
print("Last 3 characters : ", string[-3:])
middle = len(string) // 2
print("Middle 3 characters : ", string[middle-2:middle+3])