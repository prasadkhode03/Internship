'''16.	Create a text_utils.py:
o	Functions:
	count_vowels(sentence)
	count_consonants(sentence)
o	Import and test both.'''
vowels = "aeiouAEIOU"
def count_vowels(sentence):
    count = 0
    count = sum(1 for char in sentence if char in vowels)
    #OR with limitations
    # for i in sentence:
    #     if i.startswith('a') or i.startswith('e') or i.startswith('i') or i.startswith('o') or i.startswith('u'):
    #         count += 1
    return count
def count_consonants(sentence):
    count = 0
    count = sum(1 for char in sentence if char not in vowels)
    return count
