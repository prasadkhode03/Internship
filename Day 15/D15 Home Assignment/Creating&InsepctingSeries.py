#🔹 Part A: Creating and Inspecting Series/DataFrames
'''1.	Create a Series
o	Create a Pandas Series from a list of 5 city names.'''
import pandas as pd
city = ["Mumbai", "Pune", "Nashik", "Pimpalgaon", "Chalisgaon"]
myseries = pd.Series(city)
print(myseries)


'''2.	Create a DataFrame
o	Create a DataFrame called students with columns:
	Name (string), Age (int), Marks (float)'''
students = {"Name" : ["Piyush", "Prasad", "Jayesh", "Shubham"],
            "Age" : [17, 16, 18, 20],
            "Marks" : [76.80, 91.02, 81.30, 82.12]}
df = pd.DataFrame(students)
print(df)


'''3.	Check Properties
o	Print:
	.shape
	.columns
	.dtypes
	.info()
	.describe() (for numeric columns)'''
print("\nShape : ", df.shape)
print("\nTotal Columns : ", df.columns)
print("\nInformation : ", df.info())
print("\nDescription : \n", df.describe())

