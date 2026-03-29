print("TYPES OF FUNCTIONS")
print("FUNCTION WITHOUT PARAMETERS")
def python():
    print("Hello World")
python()
print("-----")
print("FUNCTION WITH ONE PARAMETERS")
def simple(name):
    print("Hello",name)
simple("Mageshwari")
print("-----")
print("FUNCTION WITH MULTIPLE PARAMETERS")
def bio(name,initial):
    print("I am ",name,initial)
bio("Mageshwari","M")
print("-----")
print("FUNCTION WITH RETURN VALUE")
def add(a,b):
    return a+b
result=add(10,5)
print("The sum =",result)
print("-----")
print("FUNCTION WITHOUT PARAMETER BUT WITH RETURN")
def number():
    return 10
print(number())
print("-----")
print("FUNCTION WITH PARAMETER AND RETURN")
def square(n):
    return n*n
print(square(6))
print("-----")
