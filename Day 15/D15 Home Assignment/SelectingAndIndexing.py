#🔹 Part B: Selecting and Indexing
'''4.	Column Selection
o	From the students DF, select the Name column and print it.'''
import pandas as pd
students = {"Name" : ["Piyush", "Prasad", "Jayesh", "Shubham"],
            "Age" : [17, 16, 18, 20],
            "Marks" : [76.80, 91.02, 81.30, 82.12]}
df = pd.DataFrame(students)
print("Name Column of Student DataFrame : \n", df["Name"])


'''5.	Row Selection by Position
o	Use .iloc to print the first 3 rows.'''
print(df.iloc[:3])


'''6.	Row Selection by Label
o	Set Name as the index and use .loc to fetch a student by name.'''
df.set_index("Name", inplace=True)
student_data = df.loc["Prasad"]
print(student_data)


'''7.	Conditional Selection
o	Select students with Marks > 75.
o	Select students with Age <= 20.'''
print("\nStudent with marks > 75 : ", df.Marks[df.Marks>75])
print("\nStudent with marks <= 20 : ", df.Marks[df.Marks<=20])