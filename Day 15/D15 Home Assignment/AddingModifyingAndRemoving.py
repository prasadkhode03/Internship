#🔹 Part C: Adding, Modifying, and Removing Columns
'''8.	Add a New Column
o	Add a column Pass which is True if Marks >= 40 else False.'''
import pandas as pd
students = {"Name" : ["Piyush", "Prasad", "Jayesh", "Shubham"],
            "Age" : [17, 16, 18, 20],
            "Marks" : [76.80, 32.03, 81.30, 28.12]}
df = pd.DataFrame(students)
df["Pass"] = df["Marks"] >= 40
print(df)


'''9.	Modify an Existing Column
o	Increase every student’s marks by 5.'''
df.Marks = df.Marks + 5
print(df)


'''10.	Remove a Column
o	Drop the Age column and print the resulting DF.'''
print(df.drop("Age", axis = 1))
