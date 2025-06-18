'''14.	Merge Two Files
o	Read from file1.txt and file2.txt
o	Merge their contents and write to merged.txt'''

with open("file1.txt", "r") as file1:
    f1data = file1.read()

with open("file2.txt", "r") as file2:
    f2data = file2.read()

with open("merged.txt", "w") as merged_file:
    merged_file.write(f1data + "\n\n" + f2data)

print("Read from file1.txt amd file2.txt and merged it to merged.txt")


