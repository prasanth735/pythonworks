from re import *

date=input("enter date")

rule="(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-((19|20)[0-9]{2})"

matcher=fullmatch(rule,date)

print("invalid" if matcher==None else "valid")