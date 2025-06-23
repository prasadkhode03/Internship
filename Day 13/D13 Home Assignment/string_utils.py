#🔹 Part F: Real-World Practice
'''13.	Create a string_utils.py:
o	count_characters(s) → returns character count.
o	count_words(s) → returns word count.
o	reverse_string(s) → returns the reversed version.
o	Import and test these in main.py.'''
def count_character(s):
	return len(s)
def count_words(s):
	return len(s.split())
def reverse_string(s):
	reverse = s[::-1]
	return reverse
