
# # # #addition

def add (n1,n2):
    res=n1+n2
    return res

print(add(100,200))
 

# # # #subtraction

def sub (n1,n2):
    res=n1-n2
    return res

print(sub(10,5))


 
# # #  #division


def div (n1,n2):
    res=n1/n2
    return res

print(div(100,10))



# # # #multipllication

def mlt(n1,n2):
    res=n1*n2
    return res

print(mlt(2,5))

# # ##


def smart_sub(n1,n2):
    res= n1-n2 if n1>n2 else n2-n1
    return res

print(smart_sub(5,100))


# #cube

def qb(num=2): #qb defult value 2
    res=num**3
    return res


print(qb())


# # Nth power

def nth_power(num,n=2): #n defult value 2
    res=num**n
    return res

print(nth_power(3,3))

# #oneth_smallest_num

def oneth_digit_smallest_num (n1,n2):
    r1=n1%10
    r2=n2%10
    res= n1 if r1<r2 else n2
    return res 

print(oneth_digit_smallest_num(1248,1246))


# century year

def century_year(yr):
    res=True if yr%100==0 else False
    return res
print(century_year(2100))