# non repeat charecter

text="abcacgh"

w={}

for ch in  text:
    if ch in w:
        w[ch]+=1
    else:
        w[ch]=1
print(w)

for  k,v in w.items():
    if (v==1):
        print(k)

