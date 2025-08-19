import pandas as pd

'''Create a Series:
Create a Series of 5 temperatures (in Celsius).
Name the Series “Temp”.'''

Temp = pd.Series([24, 36, 26, 28, 32, 30], index = ['temp1', 'temp2', 'temp3', 'temp4', 'temp5', 'temp6'])

# print(Temp.to_string(index = False))


'''Create a DataFrame:
Create a DataFrame with columns: Products, Price, and Stock.
Add 5 sample rows.'''

data = {
    "Products" : ["Laptop", "TV", "Smartphone", "Speaker", "Headphone", "Mouse", "Keyboard", "Pen", "Laptop Bag"], #
    "Price" : [40950, 60450, None, 1200, 780, 600, 800, 50, 950], #Numerical
    "Stock" : [20, 45, 30, 55, 100, 40, 50, 700, 10]

}
df = pd.DataFrame(data)
print(df)


'''Inspect the DataFrame:
Use .head() and .tail() to view your data.
Use .info() and .describe() to understand the structure'''

# print(df.head())
# print(df.tail())

# print(df.info())
# print(df.describe())


'''Selection and Indexing:
Select only the Product column.
Select the first 3 rows using .iloc.
Select Price greater than 3000.'''

# print(df['Products'])
# print(f"\n\n{df.iloc[:3]}")
print(f"\n\n{df[df['Price'] > 3000]}")