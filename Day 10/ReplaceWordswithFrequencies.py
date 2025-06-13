'''Replace Words with Frequencies
Input: "cat dog cat rat dog cat"
Output: "3 2 3 1 2 3"
'''
input_string = "cat dog cat rat dog cat"
print("Input : \"",input_string,"\"")
input = input_string.split()

my_list = [str(input.count(word)) for word in input]
string = " ".join(my_list)

print("Output : \"",string,"\"")



