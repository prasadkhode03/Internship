#🔹 Part C: Finally Block Use
'''6.	Simulate Locking/Unlocking
lock = False
o	In try: set lock = True and simulate an error (e.g., 1 / 0)
o	In finally: set lock = False and print "Resource released".'''
lock = False
try:
    lock = True
    div = 1 / 0
except ZeroDivisionError as e:
    print("Exception :", e)
finally:
    lock = False
    print("Resource released")

'''7.	File Always Closes
o	Open a file (use open("sample.txt", "w")) in try.
o	Write to it, raise an error manually using raise
o	In finally, close the file and print "File closed".'''
try:
    file = open("sample.txt", "w")
    file.write("Hello, Welcome to Python Learning.")
    raise Exception("File does not found")
except Exception as e:
    print("Error occurred :", e)
finally:
    file.close()
    print("File closed.")