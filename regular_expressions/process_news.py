from re import*

f=open("C:\\Users\\user\\Desktop\\my python\\regular_expressions\\news.txt","r")

rule="[0-9]{5}"

# for line in f:
#     train_no=line.rstrip("\n").split(" ")
#     for n in train_no:
#         matcher=fullmatch(rule,n)
#         if matcher!=None:
#             print(n)
    

for line in f:
    words=line.rstrip("\n")
    matcher=finditer(rule,words)
    for m in matcher:
        print(m.group())
  