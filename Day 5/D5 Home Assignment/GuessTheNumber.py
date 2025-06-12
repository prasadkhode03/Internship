'''11.	Guess the Number Game
•	Set a secret number (e.g., 7)
•	Let the user guess until they get it right
•	Print "Too high" or "Too low" for wrong guesses
•	Print "Correct!" when guessed'''

secretNum = 75
num = count = 0
while(num!=secretNum):
    num = int(input("Guess the Number : "))
    count += 1
    if(num>secretNum):
        print("Too High!")
    elif(num<secretNum):
        print("Too Low!")
    else:
        print(f"Correct! Secret Number is {secretNum}")
print(f"You win in {count} counts..!")
