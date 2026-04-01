import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", None, "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", None]
})


# print(df.isna())
# print(df.isnull())

# count the issing values
print(df.isna().sum())   # it will give the count of missing values in each column
print(df.isna().sum(axis=1))   # it will give the count of missing values in each row
print(df.isna().sum().sum())   # it will give the total count of missing values in the dataframe

