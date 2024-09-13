num=153
sum=0
while(num!=0):
    last_digit=num%10
    digit=last_digit**3
    sum=sum+digit
    num=num//10
print(sum)
 