def operator(*args,**kwargs):
    digit=1
    for n in args:
        if kwargs.get("operator")=="+":
            digit+=n
        elif kwargs.get("operator")=="-":
            digit-=n
        elif kwargs.get("operator")=="*":
            digit=digit*n
        elif  kwargs.get("operator")=="/":
            digit=1
            digit/=n
        elif  kwargs.get("operator")=="%":
            digit%=n
    return digit


print(operator(1,2,3,4,operator="*"))

