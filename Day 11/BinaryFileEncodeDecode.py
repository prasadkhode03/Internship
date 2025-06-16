text1 = "Hello World Binary"
text2 = "\nWelcome to Python Programming"

with open("Binary.bin", "wb+") as writeFile:
    writeFile.write(text1.encode())
    writeFile.write(text2.encode())
   

with open("Binary.bin", "rb+") as readFile:
    decodeFile = readFile.read()
    print(decodeFile.decode())   
    
