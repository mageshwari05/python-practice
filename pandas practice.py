import pandas as pd

print("CREATE DATAFRAME")

data = {
    "Name":["Ram","Sam","Raj"],
    "Marks":[80,90,85],
    "Age":[20,21,22]
}

df = pd.DataFrame(data)
print(df)

print("------")

print("PRINT NAME COLUMN")
print(df["Name"])

print("------")

print("PRINT FIRST ROWS")
print(df.head())

print("------")

print("ADD NEW COLUMN")
df["Grade"] = ["A","A","B"]
print(df)

print("------")

print("MAXIMUM MARKS")
print(df["Marks"].max())
