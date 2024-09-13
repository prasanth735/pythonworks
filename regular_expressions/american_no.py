from re import *

phone_no=input("enter number")


rule="(+1)[0-9]{10}"


matcher=fullmatch(rule,phone_no)
print("invalid" if matcher==None else "valid")

