arr=[1,2,5,6,4]
arr.sort()
i=0
while(i<len(arr)-1):
    j=i+1
    ith_lmnt=arr[i]
    jth_lmnt=arr[j]
    dif=jth_lmnt-ith_lmnt

    if(dif!=1):
        print(f"{ith_lmnt+1} is missing number")
        break
    i+=1


      