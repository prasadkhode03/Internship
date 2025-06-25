#🔹 Part D: Handling Missing Values
'''11.	Introduce Missing Values
o	Create a DF with columns Name, Age, Marks where some Age and Marks values are NaN.'''
import pandas as pd
import numpy as np
person = {"Name" : ["Om", "Prasad", "Anuj", "Atharva", "Piyush", "Jayesh"],
          "Age" : [17, np.nan, np.nan, 20, 16, np.nan ],
          "Marks" : [np.nan, 94.32, np.nan, 45.36, 74.21, 46.89],
          "Class" : ['A', 'A', 'B', 'B', 'A', 'B']
}
df = pd.DataFrame(person)


'''12.	Check for Missing Values
o	Use .isnull() and .sum() to count NaNs.'''
print("Null Values in Person Data Frame : \n", df.isnull())
missing_values = df.isnull().sum()
print("Count of NaNs in Person : \n", missing_values)


'''13.	Fill Missing Values
o	Fill NaN in the Marks column with the average marks.'''
average_marks = df['Marks'].mean()

df['Marks'] = df['Marks'].fillna(average_marks)

print(df)


'''14.	Drop Missing Values
o	Drop rows where any NaN occurs.'''
df = df.dropna()
print(df)

#🔹 Part E: Aggregation and Grouping
'''15.	Summary Stats
o	Find the total, average, max, and min marks from the DF.'''
print("\n\nTotal : ", np.sum(df.Marks))
print("Average : ", np.average(df.Marks))
print("Maximum Marks : ", np.max(df.Marks))
print("Minimum Marks : ", np.min(df.Marks))


'''16.	Grouping
o	Add a column Class (e.g., Class A or Class B).
o	Group the DF by Class and compute the average marks per class.'''
average_marks_per_class = df.groupby('Class')['Marks'].mean()
print()
print(average_marks_per_class)
