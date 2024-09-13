num=1234567831
sum=0
while(num!=0):
    last_digit=num%10
    sum=sum+last_digit
    num=num//10
print(sum)

    
# sum=0
# number=str(num)
# for n in number:
#     sum+=int(n)
# print(sum)