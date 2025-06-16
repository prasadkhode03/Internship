with open("FileHandlingModes.jpg", "rb") as file:
    readData = file.read() #Reading Data from one file
    
with open("Image.jpg", "wb") as file:
    file.write(readData) #Writing Data onto another file
