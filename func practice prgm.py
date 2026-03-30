print("TO CHECK A NUMBER ODD OR EVEN")
def check(number):
    if number % 2 == 0:
        print("Even number:", number)
    else:
        print("Odd number:", number)

check(7)   # function call
print("-----")


print("TO FIND A SQUARE OF A NUMBER")
def find(n):
    return n * n

result = find(4)
print("The square of 4 is:", result)
print("-----")


print("MULTIPLICATION TABLE OF 5")
def table(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)

table(5)   # function call
print("-----")


print("FIND LARGEST NUMBER")
def largest(a, b):
    if a > b:
        print("a is big:", a)
    else:
        print("b is big:", b)

largest(10, 20)   # function call
print("-----")


print("SUM OF NUMBERS FROM 1 TO n")
def add(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    print("Sum =", sum)
add(5)  
print("-----")
print("SIMPLE CALCULATOR USING FUNCTION")
num1 = int(input("Enter a value: "))
num2 = int(input("Enter b value: "))
print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
choice = int(input("Enter your choice: "))
def add(a, b):
    print("Addition =", a + b)
def sub(a, b):
    print("Subtraction =", a - b)
def mul(a, b):
    print("Multiplication =", a * b)
def div(a, b):
    print("Division =", a / b)
if choice == 1:
    add(num1, num2)
elif choice == 2:
    sub(num1, num2)
elif choice == 3:
    mul(num1, num2)
elif choice == 4:
    div(num1, num2)
else:
    print("Invalid choice !!!")
