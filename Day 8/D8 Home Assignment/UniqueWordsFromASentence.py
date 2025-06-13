'''14. Unique Words from a Sentence
o	Ask user for a sentence
o	Convert it into a set of unique words using split() and set()'''

#Sentence : The manager manager the team with great skill skill and patience patience.
sentence = input("Enter a sentence which includes repetitive words: ")
uni_set = set(sentence.split())
print(uni_set)
