#3.	Leap Year Checker

#Function is_leap(year) returns True if the year is a leap year, else False.
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter the Year : "))
checkLeap = is_leap(year)

if(checkLeap):
    print("Leap Year")
else:
    print("Not a Leap Year")
