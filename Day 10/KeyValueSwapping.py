my_dict = {"a" : 1, "b" : 2, "c" : 1 }

new_dict = {}
for key, value in my_dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
print(new_dict)

