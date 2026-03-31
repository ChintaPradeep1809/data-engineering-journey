import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})
#print(df)
#print(df[["Name", "Age"]])
#under the differenece
# print(df[["Name"]])
# print(df["Name"])


print(df.shape)
print(df.columns)
print(df.shape[0])
print(df.shape[1])

# info and describe are used to get the summary of the dataframe 
#  info() is used to get the information about the dataframe like the number of non-null values, data types of each column, memory usage etc.
#  describe() is used to get the statistical summary of the dataframe like count, mean, std,
#     min, 25%, 50%, 75% and max values of the numerical columns in the dataframe.
print(df.info())
print(df.describe())
