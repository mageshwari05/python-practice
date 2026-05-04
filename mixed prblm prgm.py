print("MIXED PRACTICE")
# 1. Function + String (Palindrome)
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
p = input("Enter a word: ")
palindrome(p)
print("------")
# 2. List + Loop (Sum of list)
a = [10, 20, 30, 40]
total = 0
for i in a:
    total += i
print("Sum of list:", total)
print("------")
# 3. Dictionary (Frequency)
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
# 4. File Handling
file = open("data.txt","w")
file.write("Python Programming")
file.close()
file = open("data.txt","r")
print("File content:", file.read())
file.close()
print("------")
# 5. List + Logic (Second largest)
a = [5, 10, 15, 20]
a.sort()
print("Second largest:", a[-2])
