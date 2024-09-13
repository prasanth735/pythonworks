#list >> []

colors=["red","green","blue","white","red","white"]
#         0      1      2       3       4       5 >>> index numbers
print(colors) # check allow duplication & insertion order
print(colors[2]) #retrieve

colors[1]="purple" #updation
print(colors) 


expenses=[12000,13000,23000,24000,25000,32000,23000]

for i in range(0,len(expenses)):
    print(expenses[i])


for exp in expenses:
    print(exp)


for i in range(0,len(expenses)):
    if expenses[i]>15000:
        print(expenses[i])


for i in range(0,len(expenses)):
    if expenses[i] in range(15000,25000):
    # if expenses[i]>15000 and expenses[i]<25000:
            print(expenses[i])


max_exp=max(expenses) # maximum amt
print(max_exp)

min_exp=min(expenses) #minimum amt
print(f"minnimum is {min_exp}")

total=sum(expenses) #total amt
print(total)

avg= total/len(expenses) # average amt
print(avg)



items=["ball","bat","stumps","helmet","arc","cricketball"]

longest_word=max(items,key=lambda w:len(w))
print(longest_word)

min_word=min(items,key=lambda w:len(w))
print(min_word)


   