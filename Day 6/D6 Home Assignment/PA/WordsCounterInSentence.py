#4.	Count Words in a Sentence
#Function count_words(sentence) returns total number of words in the input.

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "Hello Guys, Welcome to Python Programming. We are learning about functions!"
print("Total words =",count_words(sentence))