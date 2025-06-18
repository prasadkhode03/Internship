'''6. Count Words, Lines, Characters
o	From a file sample.txt, print:
	Total lines
	Total words
	Total characters'''
file = open("sample.txt", "r")
lines = 0
for i in file:
    lines += 1

file.seek(0)
result = file.read()
words = len(result.split())
characters = len(result)
print("Total number of lines :", lines)
print("Total number of words :", words)
print("Total number of character :", characters)