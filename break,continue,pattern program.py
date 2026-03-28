print("PRINT NUMBERS FROM 1 TO 10 AND STOP AT 7 USING BREAK")
i=1
while(i<=10):
    if(i==7):
        break
    print(i)
    i=i+1
print("-----")
print("PRINT NUMBERS FROM 1 TO 10 AND SKIP AT 7 USING CONTINUE")
i=1
while(i<=10):
    if(i==5):
        i=i+1
        continue
    print(i)
    i=i+1
print("-----")
print("SQUARE PATTERN")
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
print("ANOTHER PATTERN ")
for i in range (1,6):
    for j in range(i):
        print("*",end="")
    print()
