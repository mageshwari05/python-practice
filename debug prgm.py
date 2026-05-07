print("DAY 47 DEBUGGING PRACTICE")
# 1. Syntax Error Fixed
a = 10
b = 20
print("Sum:", a + b)
print("------")
# 2. Runtime Error Fixed
try:
    num = int(input("Enter number: "))
    print(num)
except:
    print("Invalid input")
print("------")
# 3. Division Error Fixed
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except:
    print("Cannot divide by zero")
print("------")
# 4. Logical Error Fixed
a = [10, 20, 30]
total = 0
for i in a:
    total += i
print("Correct Sum:", total)
print("------")
# 5. File Error Fixed
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except:
    print("File not found")
