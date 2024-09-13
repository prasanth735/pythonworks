# leap year


def is_leap_yr (yr):
    res= True if yr%100!=0 and yr%4==0 or yr%100==0 and yr%400==0 else False
    return res

print(is_leap_yr(2024))

#fact 

# def fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact


# print(fac(5))

# #armstrong

# def is_amstrong(num):
#     digit_count=len(num)
#     num=int(num)
#     original=num
#     sum=0
#     while(num!=0):
#         last_digit=num%10
#         pow=last_digit**digit_count
#         sum=sum+pow
#         num=num//10
#     return (True if sum==original else False )

# print(is_amstrong("153"))




# #prime

# def prime(n):
#     is_prime=True

#     for i in range(2,n):
#         if n%i==0:
#             is_prime=False
#             break
#     return is_prime

# print(prime(5))





