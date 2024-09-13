from re import *

text="Kabczabc 9@7c"

# pattern="[ac]"# a or c
# pattern="[a-e]" # a to e
# pattern="[a-z]" # a to z
# pattern="[A-Z]" # A to Z
# pattern="[a-zA-Z]" # all letters
# pattern="[0-9]" # numbers
# pattern="[a-zA-Z0-9]" # alpha numeric
# Pattern="[^a-z]" # exclude a-z
Pattern="[^a-zA-Z0-9]" # special charecters


matcher=finditer(Pattern,text)
for m in matcher:
    print(m.start(),m.group())