'''Handle Missing Values:

Create a column called Salary with some NaN values.

Fill NaN values with the average salary.'''

import pandas as pd
import numpy as np

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, 30, 35, 28, 40],
    "City": ["New York", "Paris", "London", "Tokyo", "Sydney"],
    "Salary": [50000, np.nan, 60000, np.nan, 70000]
}
df = pd.DataFrame(data)

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)