# list comprehension

#[*return  *for num in lst *condition]
lst=[2,4,5,6,7,8,9]

square=[num**2 for num in lst]
print(square)

cube=[num**3 for num in lst]
print(cube)

even=[ num for num in lst if num%2==0]
print(even)

odd=[num for num in lst if num%2!=0]
print(odd)


#print names into upper case

c4=["manoj","bilal","akash","malavika","jamina"]

upper_name=[name.upper() for name in c4]
print(upper_name)

#print name by length

name_gt_5=[name for name in c4 if len(name)>5]
print(name_gt_5)

