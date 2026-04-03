#create dictionary
print("CREATE DICT")
student = {

    "name":"Mageshwari",
           "age":20,
           "city":"Salem"
}
print(student)
print("-----")
#print value using key
print("PRINT OF VALUE USING KEY")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Salem"
}
print(student["age"])
print("-----")
#add new key
print("ADD NEW KEY")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Salem"
}
student["course"] = "Python"
print(student)
print("-----")
#updaate value
print("UPDATE VALUE")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Salem"
}
student["city"] = "Chennai"
print(student)
print("-----")
#loop dict
print("LOOP DICT")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Chennai"
}
for i in student:
    print(i, student[i])
    print("-----")
#print only keys
print("PRINT ONLY KEYS")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Chennai"
}
for i in student:
    print(i)
    print("-----")
#print only values
print("PRINT ONLY VALUES")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Chennai"
}
for i in student:
    print(student[i])
    print("-----")
#count total keys
print("COUNT TOTAL KEYS")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Chennai"
}
print("Total keys =",len(student))
print("-----")
#check key exists
print("CHECK KEY FOUND")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Chennai"
}
if "age" in student:
    print("Found")
else:
    print("Not Found")
    print("-----")
#remove key
print("REMOVE KEY")
student = {
    "name":"Mageshwari",
    "age":20,
    "city":"Chennai"
}
student.pop("city")
print(student)
print("-----")
