'''12. Print a square pattern using nested for loops:
* * * *
* * * *
* * * *
* * * *'''

for i in range (4):
    for j in range (4):
        print(" * ", end = "")
    print()

print()
'''13.	Print a right-angled triangle (same as earlier) using nested loops:
   *
  ***
 *****
*******'''

n = 4
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1)) 

