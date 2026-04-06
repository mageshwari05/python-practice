print("create a tuple")
a=(1,2,3,4,5)
print(a)
print("-----")
print("print first element")
a=(1,2,3,4,5)
print(a[0])
print("-----")
print("print last element")
a=(1,2,3,4,5)
print(a[-1])
print("-----")
print("loop through tuple")
a=(1,2,3,4,5)
for i in a:
    print(i)
print("-----")
print("find length of the tuple")
a=(1,2,3,4,5)
print(len(a))
print("-----")
print("check element 3 is found")
a=(1,2,3,4,5)
if 3 in a:
    print("element is found")
else:
    print("element is not found")
print("-----")
print("count of even number (1,2,3,4,5,6,7,8)")
a=(1,2,3,4,5,6,7,8)
count=0
for i in a:
    if i%2==0:
        count=count+1
print("Even count:",count)
print("-----")
print("find the largest number (5,12,8,20,3)")
a=(5,12,8,20,3)
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print("Largest number:",largest)
print("-----")
print("find the smallest number (5,12,8,20,3)")
a=(5,12,8,20,3)
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print("Smallest number:",smallest)
print("-----")
print("sum of tuple (1,2,3,4,5)")
a=(1,2,3,4,5)
print("Sum:",sum(a))
print("-----")
