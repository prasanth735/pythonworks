from json import load

f=open("C:\\Users\\user\\Desktop\\my python\\exchange_rate\\currency.json",encoding="utf-8")

data=load(f)

print(len(data))

exchange_rate=data.get("conversion_rates")


source_currency=input("enter the source currency code ")
target_currency=input("enter target currency code  ")
amount=int(input("enter amount "))


source_currency_rate=exchange_rate.get(source_currency)
target_currency_rate=exchange_rate.get(target_currency)


exchange_value=(amount/source_currency_rate)*target_currency_rate
print(exchange_value)




