my_tuple = ("tuple", "is", "awesome")

length = []
for word in my_tuple:
     length.append(len(word))
len_tup = tuple(length)
print(len_tup)

#length = tuple((len(word) for word in my_tuple))
#print(length)