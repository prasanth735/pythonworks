from json import load

f=open("C:\\Users\\user\\Desktop\\my python\\rest_countries\\data.json",encoding="utf-8")


data=load(f)

# print(len(data))

## all country names
# for n in data:
#     print(n.get("name"))

# country_name=[c.get("name") for c in data ]
# print(country_name)


## independent countries
# for c in data:
    # if c.get("independent")==True:
        # print(c.get("name"))


## all regeon

# all_region={c.get("region") for c in data}
# print(all_region)



## asian countries

# asia_countries=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asia_countries)


#3 ukrain capital
# ukrain= [c.get("capital") for c in data if c.get("name")=="Ukraine"]
# print(ukrain)


## all country name and capital

# name_capital=[(c.get("name"),c.get("capital")) for  c in data]
# print(name_capital)


## counntry currecy

# for c in data:
#     if "currencies" in c:
#         currency_data=c.get("currencies")[0]
#         print(currency_data.get("name"),",",c.get("name"))



## countries of indian border

# india_border=[c.get("borders") for c in data if c.get("name")=="India"][0]
# # print(india_border)

# border_name=[c.get("name") for c in data if c.get("alpha3Code") in india_border]
# print(border_name)


# counties with more than 4 border

for c in data:
    if "borders" in c and len(c.get("borders"))>4:
        print(c.get("name"))

    
        





        