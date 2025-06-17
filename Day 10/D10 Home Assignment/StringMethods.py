#🔹 Part B: String Methods Practice
'''4.	split() Method
Input: "apple,banana,cherry"
o	Split the string by comma and print the list.'''
input = "apple,banana,cherry"
split = input.split()
print("Splitted List : ", split)


'''5.	join() Method
Given a list: ["red", "green", "blue"]
o	Join the list using - as separator: "red-green-blue"'''
color = ["red", "green", "blue"]
joined_list = "-".join(color)
print("\nJoined List : ",joined_list)


'''6.	replace() Method
Input: "The sky is blue"
o	Replace "blue" with "clear"'''
input = "The sky is blue"
print("\nReplaced string :", input.replace("blue", "clear"))


'''7.	lower() and upper()
o	Convert "Python Is FUN" to all lowercase and all uppercase.'''
string = "Python Is FUN"
print("\nLowercase :", string.lower())
print("Uppercase :", string.upper())


'''8.	count() and find()
For the string "banana":
o	Count how many times "a" appears
o	Find the first occurrence of "n"'''
fruit = "banana"
print("\nCount of \"a\" :", fruit.count("a"))
print("First occurrence of \"n\" :",fruit.find("n"))
