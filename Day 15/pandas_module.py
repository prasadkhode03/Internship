# ## 🐼 **What is Pandas?**

# # Pandas is a **powerful library for data analysis**. 
# # It provides:

# # * `DataFrame`: A 2D table-like structure (like a table in Excel).
# # * `Series`: A 1D array-like structure (one column).
# # * Tools for data cleaning, filtering, and analysis.



# ## ⚡️ **1️⃣ Install and Import Pandas**

# # Install
# # pip install pandas

# # Import
import pandas as pd

# ## 🔥 **2️⃣ Creating Series and DataFrames**

# #### Series

# # Creating a Series
# s = pd.Series([10, 20, 30, 40])
# print(s)

# # Creating a Series with custom index
# s = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
# print(s)

# #### DataFrame

# # Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)

# print(df)


# ## 📋 **3️⃣ Viewing and Inspecting the Data**

# First 5 rows
# print(df.head())

# # Last 5 rows
# print(df.tail())

# # Columns
# print(df.columns)

# # Info about data types
# print(df.info())

# # Statistical summary
# print(df.describe())


# ## 👇 **4️⃣ Selecting and Indexing**

# Selecting a column
# print(df['Name'])
# print(df.Name)

# Selecting multiple columns
# print(df[['Name','Age']])

# Selecting by position
# print(df.iloc[0])           # First row
# print(df.iloc[0, 1])        # First row, second column
# print(df.iloc[0:2, 1:3])    # First two rows, columns 1–2

# # Selecting by label
# print(df.loc[0])            # First row
# print(df.loc[0, 'Name'])    # Name of first person
# print(df.loc[0:1, ['Name','City']]) 


# ## 🛠️ **5️⃣ Adding and Modifying Columns**

# Add a new column
# df['Country'] = 'India'
# print(df)

# # Modify an existing column
# df['Age'] = df['Age'] + 1
# print(df)

# Drop a column
# df = df.drop(columns=['Country'])
# print(df)

# ## 🗂️ **6️⃣ Filtering and Conditional Selection**

# # Get people older than 30
# print(df[df['Age'] > 30])

# # Multiple conditions
# print(df[(df['Age'] > 25) & (df['City'] == 'Mumbai')])


# ## 🔥 **7️⃣ Sorting and Grouping**

# # Sort by Age
# print(df.sort_values(by='Age'))

# # Group by City
# print(df.groupby('City')['Age'].mean())

# ## 🐞 **8️⃣ Handling Missing Data**

import numpy as np
# data = {'Name': ['Alice','Bob','Charlie'], 'Age': [25, None, 35]}
# df = pd.DataFrame(data)

# # Check for null values
# print(df.isnull())

# # Fill null values
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# print(df)

# # Drop rows with null
# df = df.dropna()
# print(df)

# ## 💾 **9️⃣ Reading and Writing Files**

# # Read a CSV
# df = pd.read_csv('sales_data_sample.csv', encoding = "latin1")
# df = pd.read_csv("filename.csv")
# print(df)
# # # Read an Excel file
# df = pd.read_excel('filename.xlsx')
# print(df)

# # # Export to CSV
# df.to_csv('new_file.csv', index=False)
# print(df)

# # # Export to Excel
# df.to_excel('new_file.xlsx', index=False)
# print(df)


# ## ⚡️ **10️⃣ Advanced Techniques**

# #### Applying a function

# Apply a custom function
# def add_five(x): return x + 5
# df['Age'] = df['Age'].apply(add_five)
# print(df)


# #### Merging and Joining

# df1 = pd.DataFrame({'ID': [1,2], 'Name': ['Alice','Bob']})
# df2 = pd.DataFrame({'ID': [1,2], 'City': ['Delhi','Mumbai']})
# merged = pd.merge(df1, df2, on='ID')
# print(merged)

# # #### Pivot Table

table = df.pivot_table(index='City', values='Age', aggfunc='mean')
print(table)


