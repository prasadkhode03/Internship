string = "Hello, Welcome Home!"
#{"Hello": 5, "Welcome": 7, "Home!": 5}
key = string.split()
# keylen = {word: len(word) for word in key}
keylen = {}
for word in key:
    keylen[word] = len(word)
print(keylen)


