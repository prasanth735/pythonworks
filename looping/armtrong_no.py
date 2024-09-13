num=input("enter number")
digit_count=len(num)
num=int(num)
og_num=num
sum=0

while (num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
#print(sum)
print(f"{og_num} is amstrong" if sum==og_num else" not amstrong") 