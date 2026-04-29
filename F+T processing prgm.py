print("FILE + TEXT PROCESSING")

# Read file
file = open("text.txt", "r")
data = file.read()
file.close()

print("File Content:")
print(data)

print("------")

# Word count
words = data.split()
print("Word count:", len(words))

print("------")

# Line count
lines = data.split("\n")
print("Line count:", len(lines))

print("------")

# Character count
print("Character count:", len(data))

print("------")

# Vowel count
count = 0
for i in data:
    if i.lower() in "aeiou":
        count += 1
print("Vowel count:", count)

print("------")

# Count specific word
print("Count of 'Python':", data.count("Python"))

print("------")

# Replace word
new_data = data.replace("Python", "Java")
print("After replace:")
print(new_data)
