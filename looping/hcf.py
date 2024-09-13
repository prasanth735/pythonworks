n1=int(input("enter n1 "))
n2=int(input("enter n2 "))
sm_num=n1 if n1<n2 else n2
i=1
while(i<=sm_num):
    if n1%i==0 and n2%i==0:
        hcf=i
    i+=1
print(f"gcd of {n1}, {n2} = {hcf}")

lcm=(n1*n2)/hcf
print(f"lcm of {n1} , {n2} = {lcm}")