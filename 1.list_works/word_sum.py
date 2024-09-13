items=["ball","bat","stumps","helmet","arc","cricketball"]

sum=0
# for i in range(0,len(items)):
#     current_word=items[i]
#     sum=sum+len(current_word)
# print(sum)


for i in items:
    count=len(i)
    sum+=count
print(sum)