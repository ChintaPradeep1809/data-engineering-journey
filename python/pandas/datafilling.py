import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", None, "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", None]
})

# fillna() method is used to fill the missing values in the dataframe

#print(df.fillna("Unknown"))   # it will fill the missing values with "Unknown"
#print(df.fillna({"Name":"Unknown", "City":"Smp" }))  # it will fill the missing values in 'Name' column with "Unknown" and in 'City' column with "Smp"

# df["Name"]=df["Name"].fillna("Not Available")  # it will fill the missing values in 'Name' column with "Not Available"
# print(df)

print(df.fillna(method='ffill'))   # it will fill the missing values with the previous value in the column
print(df.fillna(method='bfill'))   # it will fill the missing values with the next value in the column


