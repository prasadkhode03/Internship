# #if statement
# age = int(input("Enter your Age : "))
# if age>=18:
#     print("Your are eligible for Driving License")

# #if-else statement
# age = int(input("Enter your Age : "))
# if age>=18:
#     print("Your are eligible for Driving License")
# else:
#     print("Your are not eligible for Driving License")

# #if-elif-else statement
# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number :"))
# num3 = int(input("Enter Third Number :"))

# if (num1>num2 and num1>num3):
#     print(f"num1 = {num1} is Greater among three.")
# elif (num2>num1 and num2>num3):
#     print(f"num2 = {num2} is Greater among three.")
# else:
#     print(f"num3 = {num3} is Greater among three.")

is_raining = input("Is Raining (yes/no) : ")

if(is_raining == "yes" or is_raining == "YES"):
    print("Take Umbrella!")
else:
    print("Wear Sunglasses")

