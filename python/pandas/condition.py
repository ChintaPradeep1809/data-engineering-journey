import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

print(df[(df["Age"] > 20) & (df["City"] == "Chicago")])

print(df.query("Age > 20 and City == 'Chicago'"))
print(df.loc[df["Age"] > 20, ["Name", "City"]])