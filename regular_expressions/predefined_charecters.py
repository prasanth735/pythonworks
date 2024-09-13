from re import*

text="ab CaK7@#"
# pattern="\d" #0-9
# pattern= "\D" # [^0-9]
# pattern="\w" # alphanumeric[a-zA-Z0-9]
pattern="\W" #special charecters[^a-zA-Z0-9]

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())