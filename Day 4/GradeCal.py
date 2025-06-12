#Grade Calculator
print("\nNote : Marks should be out of 100.\n")
sub1 = int(input("Enter Marks of Subject 1 : "))
sub2 = int(input("Enter Marks of Subject 2 : "))
sub3 = int(input("Enter Marks of Subject 3 : "))

total = sub1 + sub2 + sub3
per = total / 3

print("\n~_~_~_~_~_Marks Of All Subjects_~_~_~_~_~")
print(f"Marks of Subject 1 = {sub1}")
print(f"Marks of Subject 2 = {sub2}")
print(f"Marks of Subject 3 = {sub3}")

print(f"\nTotal = {total}")
print(f"Percentage = {per}")
if(per>=80 and per<=100):
    print("Grade - A Grade")
elif(per>=60 and per<=79):
    print("Grade - B Grade")
elif(per>=40 and per<=59):
    print("Grade - C Grade")
else:
    print("Failed!")