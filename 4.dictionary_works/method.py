# methods

# 1 keys() >>> get all keys
# 2 values() >>>  get all values in dict
# 3 items () >>> return key and value
# 4 get()>>> return item by key >> return none if the value not there
# 5 update()
# 6 pop()>>> remove

product={"code":1001,"name":"orange","price":35}

#
for k in product.keys():
    print(k)

# 
for v in product.values():
    print(v)

#
for k,v in product.items():
    print(k,v)

#
print( product.get("name"))

# update
product["price"]=50
print(product)

product.update({"name":"oranges"})
print(product)

#
product.pop("price")
print(product)
