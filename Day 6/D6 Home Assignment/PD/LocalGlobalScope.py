#🔹 Part E: Code & Scope Logic
'''11.	Local vs Global Debugging
Create a global variable x = 50
•	Define function that modifies x locally
•	Define another that uses global x
•	Print x before and after both functions'''

x = 50

print("x before functions:", x)
def local_x():
    x = 100
    x += 200
    print("Local x modified:", x)

def global_x():
    global x
    x += 200
    print("Global x modified:",x)

local_x()
global_x()

print("x after functions:", x)
