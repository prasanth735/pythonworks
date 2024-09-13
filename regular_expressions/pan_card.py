from re import *
pan_number=input("enter your pan number")
rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]"

matcher=fullmatch(rule,pan_number)
print("invalid" if matcher==None else "valid")

