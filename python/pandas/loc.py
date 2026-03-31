import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

# loc is used to select rows and colums by label or column name 
# loc includes ending index while slicing

# select the row with index 0
print(df.loc[0])
# select the row with index 1 and 2
print(df.loc[1:2])
# select the column with name "Name" 
# print(df.loc[:, "Name"])
print(df.loc[0, "Name"])
# print(df.loc[df["Age"] > 30, "Name"])
