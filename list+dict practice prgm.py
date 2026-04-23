# LIST PRACTICE
print("LIST OPERATIONS")

a = [10, 20, 30, 40, 50]
print("List:", a)

# Add element
a.append(60)
print("After append:", a)

# Remove element
a.remove(20)
print("After remove:", a)

# Find length
print("Length:", len(a))

# Sum
print("Sum:", sum(a))

# Maximum
print("Max:", max(a))

# Minimum
print("Min:", min(a))

print("------")

# Loop through list
print("List elements:")
for i in a:
    print(i)

print("------")

# DICTIONARY PRACTICE
print("DICTIONARY OPERATIONS")

student = {
    "name": "Ram",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)

# Add new key
student["marks"] = 90
print("After adding marks:", student)

# Access value
print("Name:", student["name"])

# Update value
student["age"] = 21
print("Updated age:", student)

# Loop through dictionary
print("All data:")
for key in student:
    print(key, ":", student[key])
