import pandas as pd
ser = pd.Series([1, 2, 3, 4, 5])
print(ser)
print(ser[0])
print(ser[1:4])
print(ser.dtype)


ser2 = pd.Series(["Alice", "Bob", "Charlie"])
print(ser2)
print(ser2[0])
print(ser2[1:3])


# parameters of series data, index, dtype, name, copy
ser3 = pd.Series([1, 2, 3], index=["a", "b", "c"], dtype=float, name="Numbers")
print(ser3)
print(ser3.index)

# properties of series data, values, index, dtype, name
print(ser3.values)
print(ser3.index)
print(ser3.dtype)
print(ser3.name)
