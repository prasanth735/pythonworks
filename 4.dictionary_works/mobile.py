mobile={"id":1001,"name":"iphone15","price":100000,"imei":12345,"processor":"apple"}

# print all values and pairs 
# print name
# print price
# update price as 85000
#remove imei


for k,v in mobile.items():
    print(k,v)

print(mobile.get("name"))

print(mobile.get("price"))

mobile.update({"price":85000}) # mobile["price"]=85000
print(mobile)

mobile.pop("imei")
print(mobile)

mobile.update({"offer":1000})
print(mobile)

mobile["price"]+=1000
print(mobile)

print("color" in mobile)