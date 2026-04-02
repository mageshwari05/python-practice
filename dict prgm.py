print("CREATE A DICTIONARY AND PRINT IT")
dict={"name":"mageshwari","age":18,"section":"A"}
print(dict)
print("-----")

print("PRINT VALUE USING KEY")
fav={"Chocolate":"kitkat","ice cream":"blackcurrent","juice":"pulpy orange"}
print(fav["Chocolate"])
print("-----")

print("ADD NEW KEY AND VALUE")
fav={"Chocolate":"kitkat","ice cream":"blackcurrent","juice":"pulpy orange"}
fav["cake"]="brownie"
print(fav)
print("-----")

print("LOOP THROUGH DICTIONARY")
fav={"Chocolate":"kitkat","ice cream":"blackcurrent","juice":"pulpy orange"}
for i in fav:
    print(i,fav[i])
print("-----")

print("TO PRINT KEYS AND VALUES SEPERATELY")
fav={"Chocolate":"kitkat","ice cream":"blackcurrent","juice":"pulpy orange"}
print(fav.keys())
print(fav.values())
print("-----")
