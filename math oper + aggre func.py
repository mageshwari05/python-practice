import numpy as np

# =====================================
# Exercise 1: Mathematical Operations
# =====================================
print("===== Exercise 1 =====")

arr = np.array([5, 10, 15, 20, 25])

print("Original Array:", arr)
print("Add 5:", arr + 5)
print("Subtract 2:", arr - 2)
print("Multiply by 3:", arr * 3)
print("Divide by 5:", arr / 5)
print("Square:", arr ** 2)

# =====================================
# Exercise 2: Array Operations
# =====================================
print("\n===== Exercise 2 =====")

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print("Array A:", a)
print("Array B:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# =====================================
# Exercise 3: Aggregation Functions
# =====================================
print("\n===== Exercise 3 =====")

marks = np.array([70, 85, 90, 65, 95])

print("Marks:", marks)
print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))

# =====================================
# Day 3 Mini Project
# =====================================
print("\n===== Day 3 Mini Project =====")

student_marks = np.array([78, 82, 91, 67, 88, 95, 73, 80])

print("Student Marks:", student_marks)

print("Total Marks:", np.sum(student_marks))
print("Average Marks:", np.mean(student_marks))
print("Highest Marks:", np.max(student_marks))
print("Lowest Marks:", np.min(student_marks))
print("Standard Deviation:", np.std(student_marks))
print("Variance:", np.var(student_marks))

print("\nAfter Adding 5 Bonus Marks:")
print(student_marks + 5)

print("\nAfter Multiplying Marks by 2:")
print(student_marks * 2)
