from re import *

variable_name=input("enter variable name  ")

rule="[a-zA-Z]{1}[a-zA-Z0-9]*"

matcher=fullmatch(rule,variable_name)

print("invalied" if matcher==None else "valid")



