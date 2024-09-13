# 2nd repeated charecter

text="ABCABD"

wc={}

dup_ch=[]

for ch in text:
    if ch in wc:
        wc[ch]+=1
        dup_ch.append(ch)
    else:
        wc[ch]=1


print(dup_ch[1])