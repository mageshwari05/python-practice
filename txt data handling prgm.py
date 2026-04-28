print("TEXT DATA HANDLING")

# Write to file
file = open("text.txt", "w")
file.write("Python is easy\nData Science is powerful")
file.close()

print("Data written")

print("------")

# Read file
file = open("text.txt", "r")
data = file.read()
print(data)
file.close()

print("------")

# Count words
words = data.split()
print("Word count:", len(words))

print("------")

# Count lines
lines = data.split("\n")
print("Line count:", len(lines))

print("------")

# Count characters
print("Character count:", len(data))

print("------")

# Convert to uppercase
print("Uppercase:")
print(data.upper())
