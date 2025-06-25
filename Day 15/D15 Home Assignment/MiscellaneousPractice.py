#🔹 Part F: Miscellaneous Practice
'''17.	Sorting
o	Sort the DF by Marks in ascending and then in descending order.'''
import pandas as pd
students = {"Name" : ["Piyush", "Prasad", "Jayesh", "Shubham"],
            "Age" : [17, 16, 18, 20],
            "Marks" : [76.80, 32.03, 81.30, 28.12]}
df = pd.DataFrame(students)
print("Asceding Order of Marks : \n", df.Marks.sort_values())
print("Descending Order of Marks : \n", df.Marks.sort_values(ascending=False))


'''18.	Rename Columns
o	Rename columns Name -> Student Name, Marks -> Total Marks.'''
df = df.rename(columns={'Name': 'Student Name', 'Marks': 'Total Marks'})
print(df)


'''19.	Export DF
o	Export the final DF to a .csv file named student_records.csv.'''
df.to_csv('student_records.csv', index=False)
print("DataFrame exported to student_records.csv")


'''20.	Apply a Function
o	Use .apply() to categorize marks:
	Marks >= 80: Excellent
	Marks >= 60: Good
	Marks >= 40: Pass
	Marks < 40: Fail'''
def categorize_marks(marks):
    if marks >= 80:
        return 'Excellent'
    elif marks >= 60:
        return 'Good'
    elif marks >= 40:
        return 'Pass'
    else:
        return 'Fail'
df['Category'] = df['Total Marks'].apply(categorize_marks)
print(df)


'''21.	Check Duplicates
o	Identify and remove duplicate rows in the DF.'''
duplicate_rows = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_rows}")

print("Duplicate rows:")
print(df[df.duplicated()])

df = df.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(df)


'''22.	Merge Two DataFrames
o	Create another DF with columns Name and Class Teacher.
o	Merge both DFs on the Name column.'''

data1 = {
    "Name" : ["Sachin", "Prasad", "Piyush", "Om", "Ranjit"],
    "Age": [20, 21, 19, 22, 20],
    "Total Marks" : [85, 90, 78, 92, 88]
}
df1 = pd.DataFrame(data1)

data2 = {
    "Name" : ["Sachin", "Prasad", "Piyush", "Om", "Ranjit"],
    "Class Teacher" : ["Prof. Katkade", "Mr. Sangale", "Ms. Ushir", "Mr. Jadhav", "Ms. Vidhate"]
}
df2 = pd.DataFrame(data2)

df = pd.merge(df1, df2, on="Name")
print(df)
