import pandas as pd
df = pd.DataFrame({
    "Name": ["Alice", None, "Charlie","Pradeep","Pradeep","Pradeep"],
    "Age": [25, 30, 35,20,20,10],
    "City": ["New York", "Los Angeles", None,"Hyderabad","Hyderabad","Hyderabad"]
})

# print(df["Name"].str.lower())   # it will convert the values in 'Name' column to lowercase
# print(df["City"].str.upper())   # it will convert the values in 'City' column to uppercase
# print(df["Name"].str.strip())   # it will remove the leading and trailing spaces from the values in 'Name' column
# print(df["City"].str.replace(" ", "_"))   # it will replace the spaces in
 
# print(df["Name"].str.contains("a", case=False))   # it will check if the values in 'Name' column contain the letter 'a' (case insensitive)
# print(df["City"].str.startswith("a"))   # it will check if the values in

# # duplicated 
# print(df.duplicated())   # it will check for duplicate rows in the dataframe
# print(df.duplicated(subset=['Name']))   # it will check for duplicate values in 'Name' column
# print(df.duplicated(subset=['City']))   # it will check for duplicate values in 'City' column


# print(df.drop_duplicates())   # it will drop the duplicate rows from the dataframe
print(df.drop_duplicates(subset=['Name']))   # it will drop the duplicate values in ' keep first occurrence and drop the rest
print(df.drop_duplicates(subset=['Name'], keep='first'))   # it will keep the first occurrence of the duplicate values in 'Name' column and drop the rest




