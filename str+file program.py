print("STRING + FILE PRACTICE")

# Write string to file
file = open("data.txt","w")
string = "Learn Python Programming"
file.write(string)
file.close()

print("Data Written to File")

print("------")

# Read from file
file = open("data.txt","r")
data = file.read()
print("File Content:",data)
file.close()

print("------")

# Count characters
print("Length:",len(data))

print("------")

# Count words
words = data.split()
print("Word Count:",len(words))

print("------")

# Count vowels
count = 0
for i in data:
    if i.lower() in "aeiou":
        count = count + 1

print("Vowel Count:",count)

print("------")

# Convert uppercase
print("Uppercase:",data.upper())

print("------")

# Reverse string
print("Reverse:",data[::-1])
