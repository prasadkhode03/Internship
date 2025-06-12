#Printing list elements using for loop
# my_list = ["Apple", "Banana", "Cherry", "Chickoo", "Kivi", "Papaya", "Mango", "Black Berry", "Jack Fruit", "Dragon Fruit"]
# for i in range (len(my_list)):
#     print(my_list[i], end = " ")
# print(f"\nLength of my_list : {len(my_list)}")


#Overwriting a new element with exisiting at a specific index
# new_list = [12, 32, 56, 74, 91, 35, 94, 65, 16]
# print("Before Adding : ", new_list)
# new_list[2] = 45
# print("After Adding : ", new_list)

# #Printing last 3 elements
# print(new_list[-3:]) #From left to right
# print(new_list[-1:-4:-1]) #From right to left

#Merging two list
# list1 = ["Prasad"]
# list2 = ["Khode", "Hello", "World"]
# list1.extend(list2)
# print(list1)


# #Removing items from the list
# demo_list = [10, 20, 3, 465, 956, 346, 45, 95, 321, 67, 49, 312, 689, 153, 2395, 596]

# print("List before Operations : ", demo_list)

# popped_element = demo_list.pop(2) # pop(index_number)
# print("Popped Element : ", popped_element)
# print("List after Popping Element : ", demo_list)

# demo_list.remove(465) #remove(value)
# print("\nList after removing Element : ", demo_list)

# del demo_list[4:] #del list_name[index_number]
# print("\nList after deleting Element : ", demo_list)

#Addition of all elemnts of the list
def listAddition(my_list):
    sum = 0
    for i in range (len(num_list)):
        sum = sum + num_list[i]
    return sum

num_list = [10, 20, 30, 40, 50]
print(f"Sum = {listAddition(num_list)}")

