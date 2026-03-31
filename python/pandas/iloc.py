import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

# iloc is used to select rows and columns by integer position
# iloc does not include ending index while slicing

# select the row with index 0
print(df.iloc[0])
# select the row with index 1 and 2
print(df.iloc[1:3])
# select the column with index 0
print(df.iloc[:, 0])
# select the value at row index 0 and column index 0
print(df.iloc[0, 0])

