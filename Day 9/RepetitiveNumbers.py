num_tuple = (12, 232, 15, 45, 12, 232, 659, 12, 456)
my_list = []
for i in range (len(num_tuple)):
    count = num_tuple.count(num_tuple[i])
    if count > 1 and num_tuple[i] not in my_list:
        my_list.append(num_tuple[i])
    
print("List of Repetitive Number : ",tuple(my_list))


