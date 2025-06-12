my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = [i**2 for i in my_list] 

for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 2
print(my_list)
