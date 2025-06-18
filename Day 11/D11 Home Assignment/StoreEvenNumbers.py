'''11.	Store Even Numbers
o	Write a program to find even numbers from 1–50
o	Save them line-by-line into even_numbers.txt'''

with open("even_numbers", "w") as file:
    file.write("Even Numbers from 1 to 50 - \n")
    for i in range(1, 50 + 1):
        if i % 2 == 0:
            file.write(f"{i}\n")

print("Even Numbers saved in file.")
