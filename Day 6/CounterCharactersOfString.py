#Write a function and give a count of character appears in a string
count = 0
def countCharacter(name):
    global count
    for i in name:
        if(i=='a'):
            count+=1
    return count
print(f"Number of 'a' in Prasad Name is : {countCharacter("Prasad")}")