try:
    num = int(input("Enter a number : "))
    print("Number : ", num)
except ValueError:
    print("Cannot convert str to int")
