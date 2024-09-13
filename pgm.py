# print("hello world")



a="abcde"
b="fghijkl"

lst1=[]
lst2=[]

for w in a:
    lst1.append(w)

for w in b:
    lst2.append(w)

word=""
count=0
for w in range(0,len(lst1)):
    for c in range(0,len(lst2)):
        count+=1
        if w==c:
            word+=lst1[w]
            word+=lst2[c]
print(word)
print(count)



