from json import load
f=open("C:\\Users\\user\\Desktop\\my python\\products\\items.json","r",encoding="utf-8")

data=load(f)
# print(len(data))

category={p.get("category") for p in data}
print(category)

electronic_product=[p for p in data if p.get("category")=="electronics"]

print(len(electronic_product))


jwellery_products= [p for p in data if p.get("category")=="jewelery"]

print(len(jwellery_products))


costly_product= [p for p in data]
highset_value=(max(costly_product,key=lambda d:d.get("price")))
print(highset_value.get("title"),highset_value.get("price"))