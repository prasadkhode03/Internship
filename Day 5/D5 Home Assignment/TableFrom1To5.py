'''14. Create a multiplication table from 1 to 5, like:
1 x 1 = 1
1 x 2 = 2
...
5 x 10 = 50'''

for i in range (1, 5 + 1):
    for j in range (1, 10 + 1):
        print(f"{i} X {j} = {i * j}")


'''15.	Print a number triangle pattern like this (for n = 4):
1
1 2
1 2 3
1 2 3 4'''

n = 6
for i in range (1, n):
    for j in range (1, i):
        print(j," ", end = "")
    print()