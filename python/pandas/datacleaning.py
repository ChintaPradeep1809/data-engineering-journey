import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", None, "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", None]
})

# parameeters of dropna() method 
# axis: 0 for rows and 1 for columns
# how: 'any' to drop if any value is missing and 'all' to drop
# if all values are missing
# subset: to specify the columns to check for missing values

print(df.dropna())   # it will drop the rows with missing values
print(df.dropna(axis=1))   # it will drop the columns with missing values
print(df.dropna(how='all'))   # it will drop the rows where all values are missing
print(df.dropna(subset=['Name']))   # it will drop the rows where the 'Name' column has missing values
