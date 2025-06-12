#Part C: Loop Control Statements

#6.	Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7.
print("Stopping Loop if the number is 7 - ")
for i in range (1, 10+1):
    if i == 7:
        break 
    print(i)

#7.	Use a for loop to print numbers from 1 to 10, but skip printing 5.
print("Skipping if the number is 5 - ")
for i in range (1, 10+1):
    if i == 5:
        continue 
    print(i)