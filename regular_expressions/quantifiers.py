from re import *

text="aaabcaabbaabd"

# pattern="a*" # any  number of a including zero 
# pattern="a{2}" # exact 2a >aa
pattern="a{2,4}" # minimum 2 maximum 4


matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())