from re import*

f=open("C:\\Users\\user\\Desktop\\my python\\regular_expressions\\numbers.text","r")

rule="(([+](91))?[0-9]{10})"

for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher !=None:
        print(number)
 