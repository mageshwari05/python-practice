print("LOGIC PRACTICE")
# 1. Check Prime Number
def prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print("7:", prime(7))

print("------")

# 2. Sum of Digits
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print("123:", sum_digits(123))

print("------")

# 3. Count Even & Odd
def count_even_odd(a):
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

e, o = count_even_odd([1,2,3,4,5,6])
print("Even:", e, "Odd:", o)

print("------")

# 4. Find Largest Word
def largest_word(s):
    words = s.split()
    max_word = words[0]
    for i in words:
        if len(i) > len(max_word):
            max_word = i
    return max_word

print("Largest word:", largest_word("learn python programming"))

print("------")

# 5. Remove Spaces from String
def remove_spaces(s):
    return s.replace(" ", "")

print("No spaces:", remove_spaces("learn python"))
