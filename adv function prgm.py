print("ADVANCED FUNCTIONS")

# Function with Parameters
def add(a,b):
    print("Sum =",a+b)

add(5,3)

print("------")

# Function with Return
def add2(a,b):
    return a+b

result = add2(10,5)
print("Return Sum =",result)

print("------")

# Default Argument
def greet(name="User"):
    print("Hello",name)

greet()
greet("Mageshwari")

print("------")

# Multiple Parameters
def student(name,age,course):
    print("Name:",name)
    print("Age:",age)
    print("Course:",course)

student("Ram",20,"Python")

print("------")

# Multiple Return Values
def calc(a,b):
    return a+b, a-b

sum,sub = calc(20,10)

print("Sum:",sum)
print("Sub:",sub)
