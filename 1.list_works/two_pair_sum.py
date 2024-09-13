lst=[3,4,5,2,6,9]

sum=int(input("enter sum"))
# count=1

lst.sort()
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         cur_sum=lst[i]+lst[j]

#         if cur_sum==sum:
#             print(lst[i],lst[j])
#             break
#         # count+=1

# # print("loop count=",count)

# count=1
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low] + lst[upp]

    if cur_sum==sum:
        print(lst[low],lst[upp])
        # break >>> for 1 pair
        low+=1
        upp-=1
    elif cur_sum<sum:
        low+=1
    elif cur_sum>sum:
        upp-=1

#     count+=1

# print(count)


