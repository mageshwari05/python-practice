import pandas as pd

print("CREATE SERIES")
data = [10,20,30,40]
s = pd.Series(data)
print(s)

print("------")

print("CREATE DATAFRAME")
data = {
    "Name":["Ram","Sam","Raj"],
    "Age":[20,21,22]
}

df = pd.DataFrame(data)
print(df)

print("------")

print("PRINT COLUMN")
print(df["Name"])

print("------")

print("PRINT FIRST ROWS")
print(df.head())

print("------")

print("DATAFRAME INFO")
print(df.info())
