print("PRINT LIST  ELEMENTS")
n=[1,2,3,4]
print(n)
print("-----")

print("FIND LENGTH OF A LIST")
N=[2,4,6,8,10]
print(len(N))
print("------")

print("FIND SUM OF LIST")
num=[1,2,3,4,5]
sum=0
for i in num:
    sum=sum+i
print("Sum=",sum)
print("-----")
print("TO PRINT LARGEST NUMBER")
a=[11,15,3,12,5]
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print("largest value is =",largest)
print("-----")

print("TO PRINT SMALLEST NUMBER")
a=[11,15,3,12,5]
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print("smalllest value is =",smallest)
print("-----")

print("COUNT OF AN EVEN NUMBER")
a=[1,2,3,4,5,6,7,8,9,10]
count=0
for i in a:
    if i%2==0:
        count=count+1
print(count)
print("-----")

print("REVERSE  OF A LIST")
a=[1,2,3,4,5]
print(a)
a.reverse()
print(a)
print("-----")

print("SORT THE LIST")
a=[6,8,2,13,45]
print(a)
a.sort()
print(a)
print("-----")

print("TO PRINT FIRST ELEMENT")
a=[10,20,30]
print(a[0])
print("-----")

print("TO PRINT LAST ELEMENT")
a=[10,20,30]
print(a[-1])
print("-----")

print("REMOVE ELEMENT IN A LIST")
a = [1,2,3,4]
a.remove(3)
print(a)
print("-----")

print("CHECK A NUMBER IN A LIST")
a = [1,2,3,4]
if 3 in a:
    print("Found")
else:
    print("Not Found")
print("-----")

