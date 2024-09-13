word="hello hai hello hai"
wrd=word.split()

wc={}

for w in wrd:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)
