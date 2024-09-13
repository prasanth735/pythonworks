prev=0
current=1
print(F"{prev} {current}",end=" ")

for i in range(1,11):
    next=prev+current
    print(next,end=" ") #end="," 
    prev=current
    current=next

print("abc", end=",") 
 