string = "learn python programming"
print("Original String:", string)

print("------")

# Length of string
print("Length:", len(string))

print("------")

# Uppercase
print("Uppercase:", string.upper())

# Lowercase
print("Lowercase:", string.lower())

print("------")

# Count words
words = string.split()
print("Word count:", len(words))

print("------")

# Count vowels
count = 0
for i in string:
    if i in "aeiou":
        count = count + 1
print("Vowel count:", count)

print("------")

# Count consonants
count = 0
for i in string:
    if i not in "aeiou ":
        count = count + 1
print("Consonant count:", count)

print("------")

# Reverse string
print("Reverse:", string[::-1])

print("------")

# Check substring
if "python" in string:
    print("Word 'python' found")
else:
    print("Not found")

print("------")

# Replace word
new_string = string.replace("python","java")
print("After replace:", new_string)
