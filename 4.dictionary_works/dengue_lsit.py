dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]

wc={}

for dst  in dengue_list:
    if dst in wc:
        wc[dst]+=1
    else:
        wc[dst]=1
print(wc)

srt_wc=sorted(wc,key= lambda k:wc.get(k),reverse=True)
print(srt_wc)

print(max([(v,k)for k,v in wc.items()])) 


