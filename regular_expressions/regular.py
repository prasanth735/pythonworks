from re import *

text="fat-cat-run-fast-catch"

pattren="at"

matcher=finditer(pattren,text)

count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)