selling_price=int(input("enter selling price"))
cost_price=int(input("enter cost price"))

profit=selling_price-cost_price
print(f"profit is {profit}")
profit_in_percentage=(profit/cost_price)*100

print(f" profit in percentage is {profit_in_percentage}")