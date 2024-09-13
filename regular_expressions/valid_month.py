from re import*
# month

# month=input("enter a month")

# rule="(0[1-9]|1[012])"

# matcher=fullmatch(rule,month)

# print("invalid" if matcher==None else "valid")


#date

# date= input("enter date ")
# rule="([1-9]|0[1-9]|1[0-9]|2[0-9]|3[01])" #([1-9]|0[0-9]|[12][0-9]|3[01])"

# matcher=fullmatch(rule,date)
# print("invalid" if matcher==None else "valid")

# year 1900- 2099

year=input("enter year")

rule="((19)[0-9]{2}|(20)[0-9]{2})"
#"((19|20)[0-9]{2})"

matcher=fullmatch(rule,year)
print("invalid" if matcher==None else "valid")


