#first recursive charecter >>> repeat


word="ABCABBDE"

w={}

for ch in word:
    if ch in w:
        print(" recursive charecter is",ch)
        break
    else:
        w[ch]=1
    
