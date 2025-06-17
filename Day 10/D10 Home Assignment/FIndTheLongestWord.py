'''16.	Find the Longest Word
•	Input a sentence
•	Find and print the longest word and its length'''
sentence = input("Enter your sentence : ")
sen_list = sentence.split()

longest = sen_list[0]
length = len(longest)

for word in sen_list:
    if len(word) > length:
        length = len(word)
        longest = word

print(f"\nLongest word is \"{longest}\" and its lengh is {length}.")
