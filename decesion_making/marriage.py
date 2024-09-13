his_age=int(input("enter his age"))
her_age=int(input("enter her age"))
married_status= int(input("select status 1 for married ,2 for 2 single"))
if his_age>=21 and her_age>=18 and married_status==2:
    print("proceed")
else:
    print("not possible")