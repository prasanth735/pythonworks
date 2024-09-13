weight=int(input("enter your weight in kg"))
height_in_cm=int(input("enter your high in cm"))

height_in_m=(height_in_cm/100)

bmi=(weight)/height_in_m**2

print(f"bmi is {bmi}")
if bmi>40:
    print("severe obese")
elif bmi>30:
    print("obesily")
elif bmi>25:
    print("over weight")
elif bmi>19:
    print("healthy")
else:
    print("under weight")


 
 