print("count vowels")
string = "python programming"
count = 0
for i in string:
    if i in "aeiou":
        count = count + 1
print("Vowels =", count)
print("Reverse String")
string = "python"
print(string[::-1])
print("Check string exists")
string = "learn python"
if "python" in string:
    print("Found")
else:
    print("Not Found")
print("Count characters")
string = "python"
count = 0
for i in string:
    count = count + 1
print("Length =", count)
print("count consonants")
string = "python"
count = 0
for i in string:
    if i not in "aeiou":
        count = count + 1
print("Consonants =", count)
print("check palindrome")
string = "python"
count = 0
for i in string:
    if i not in "aeiou":
        count = count + 1
print("Consonants =", count)
