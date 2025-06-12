# #🔹 Part D: Real-World Scenarios
# """6.	Ask for a username and password:
# o	If both are correct → "Login successful"
# o	If username is correct but password is wrong → "Wrong password"
# o	If username is wrong → "User not found" """

# #Asking for a username and password
# username = input("Enter username : ")
# password = input("Enter password : ")

# if username == "admin" and password == "pass@123":
#     print("Login successful!")
# elif username == "admin" and password != "pass@123":
#     print("Wrong password")
# elif username != "admin":
#     print("User not found")

# """7.	A shop gives discount:
# o	Total bill < 500 → No discount
# o	500 to 1000 → 5% discount
# o	Above 1000 → 10% discount
# Take bill amount as input and display final amount to be paid."""

# total_bill = float(input("Enter Total Bill : "))
# if total_bill < 500:
#     discountedAmount = total_bill
#     print(f"No Discount")
# elif total_bill >= 500 and total_bill<=1000:
#     amountOfDiscount = total_bill * 0.05
#     discountedAmount = total_bill - amountOfDiscount
# elif total_bill >1000:
#     amountOfDiscount = total_bill * 0.10
#     discountedAmount = total_bill - amountOfDiscount

# print(f"Final Amount - {discountedAmount}")


#8.	Rock-Paper-Scissors game (two players):
"""o	Take input from both players
o	Compare:
	Rock beats Scissors
	Scissors beats Paper
	Paper beats Rock
	Same → Tie"""

name1 = input("Enter Player 1 Name : ")
name2 = input("Enter Player 2 Name : ")
player1 = input(f"{name1} Enter Rock-Paper-Scissors : ")
player2 = input(f"{name2} Enter Rock-Paper-Scissors : ")

if ((player1 == "Rock") and (player2 == "Scissors")) or ((player1 == "Scissors") and (player2 == "Rock")):
    print("Rock Beats Scissors")
    if(player1 == "Rock"):
        print(f"{name1} Wins!")
    else:
        print(f"{name2} Wins!")
elif ((player1 == "Paper") and (player2 == "Scissors")) or ((player1 == "Scissors") and (player2 == "Paper")):
    print("Scissors beats Paper")
    if(player1 == "Scissors"):
        print(f"{name1} Wins!")
    else:
        print(f"{name2} Wins!")
elif ((player1 == "Rock") and (player2 == "Paper")) or ((player1 == "Paper") and (player2 == "Rock")):
    print("Paper beats Rock")
    if(player1 == "Paper"):
        print(f"{name1} Wins!")
    else:
        print(f"{name2} Wins!")
elif player1 == player2:
    print("Tie")
else:
    print("Invalid Input!")

