print("PROBLEM SOLVING")
# Fibonacci Series
def fib(n):
    a, b = 0, 1
    print("Fibonacci:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b
    print()
fib(7)
print("------")
# Armstrong Number
def armstrong(n):
    temp = n
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit**3
        n //= 10
    if sum == temp:
        return "Armstrong"
    else:
        return "Not Armstrong"
print("153:", armstrong(153))
print("------")
# Remove Duplicates
def remove_dup(a):
    new = []
    for i in a:
        if i not in new:
            new.append(i)
    return new
print("Remove duplicates:", remove_dup([1,2,2,3,4,4]))
print("------")
# Frequency of Characters
def frequency(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
print("Frequency:", frequency("python"))
print("------")
# Second Largest Number
def second_largest(a):
    a = list(set(a))
    a.sort()
    return a[-2]
print("Second largest:", second_largest([10,20,30,40]))
