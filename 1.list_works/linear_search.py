lst=[10,2,11,5,7,20]
element=int(input("enter element"))

is_present=False

for i in range(0,len(lst)):
    cur_element=lst[i]

    if cur_element==element:
        is_present=True
        break

print(is_present)