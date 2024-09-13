
# starting with k,l,m,or n
# second place must be digit that is divisible by 3
# followed by any number or alphabets

from re import *


variable_name=input("enter variable name")
rule="[k-nK-N][369][a-ZA-Z0-9]*"

matcher=fullmatch(rule,variable_name)

print("invalid" if matcher==None else "valid")