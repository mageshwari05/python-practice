print("PROBLEM SOLVING")

# Palindrome
def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(palindrome("madam"))

print("------")

# Count Even Numbers
def even_count(a):
    count = 0
    for i in a:
        if i % 2 == 0:
            count = count + 1
    return count

print("Even count:", even_count([1,2,3,4,5,6]))

print("------")

# Find Minimum
def minimum(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min

print("Minimum:", minimum([5,2,8,1,9]))

print("------")

# Sum of Digits
def sum_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum

print("Sum of digits:", sum_digits(123))

print("------")

# Count Consonants
def consonants(s):
    count = 0
    for i in s:
        if i not in "aeiou ":
            count = count + 1
    return count

print("Consonants:", consonants("python programming"))

print("------")

# Multiplication Table
def table(n):
    for i in range(1,11):
        print(n, "x", i, "=", n*i)

table(5)

print("------")

# Average of List
def average(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum / len(a)

print("Average:", average([10,20,30,40]))
