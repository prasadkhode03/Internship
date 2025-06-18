'''12.	Reverse File Content
o	Read lines from sample.txt
o	Reverse each line and write it to reversed.txt'''

with open("sample.txt", "r") as readFile:
    lines = readFile.readlines()

with open("reversed.txt", "w") as writeFile:
    for line in lines:
        reversed = line[::-1]
        writeFile.write(reversed)
    print("Readed data from sample.txt and wrote data to reversed.txt successfully!")
    
