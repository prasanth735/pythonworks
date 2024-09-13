
# infinite number of parameters in function

## args >> tuple

def add(*args):
    return sum(args)


# print(add(10,20))
# print(add(10,20,30,40))
# print(add())


def lat_sum(*args):
    sum=0
    for n in args:
        num=n%10
        sum+=num
    return sum 


# print(lat_sum(1123,345,567,760,678))

def last_digit_max(*args):
    digits=[n%10 for n in args]
    return max(digits)

# print(last_digit_max(123,134,135,18,19)) 



## kwargs>> dictionary

def add_employee(**kwargs):
    print(kwargs.get("name")) 
    print(kwargs.get("salary"))
    # print(kwargs.items())
    # print(kwargs.values())


# add_employee(id=10,name="hari",n_palce="ekm",w_place="tvm",salary=24000)


def last_digit_sort(*args,**kwargs):
    digit= [n%10 for n in args]
    value=kwargs.get("reversed")
    if value==True:
        digit.sort(reverse=True)
    else:
        digit.sort()
    return digit

print(last_digit_sort(12,13,14,17,reversed=True))