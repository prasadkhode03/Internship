'''10.	Palindrome Checker
•	Check if a string is the same when reversed (e.g., "madam", "racecar")'''
# string1 = "madam"
# string2 = "racecar"
print("Welcome to Palindrome Checker")
def PalindromeChecker(string):
    if string == string[::-1]:
        print("String is Palindrome.")
    else:
        print("String is not Palindrome.") 

string = input("What is your string? : ")
PalindromeChecker(string)