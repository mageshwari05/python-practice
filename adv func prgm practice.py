print("FUNCTION PRACTICE")

# Square Function
def square(n):
    return n*n

print("Square:", square(5))

print("------")

# Cube Function
def cube(n):
    return n*n*n

print("Cube:", cube(3))

print("------")

# Even or Odd
def check(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

check(10)

print("------")

# Add Two Numbers
def add(a,b):
    return a+b

print("Sum:", add(5,7))

print("------")

# Largest Number
def largest(a,b):
    if a>b:
        return a
    else:
        return b

print("Largest:", largest(10,20))

print("------")

# Reverse String
def reverse(s):
    return s[::-1]

print("Reverse:", reverse("python"))

print("------")

# Count Vowels
def vowels(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count = count + 1
    return count

print("Vowels:", vowels("python programming"))
