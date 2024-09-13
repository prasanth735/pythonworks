# kerala vehicle reg no

# start with KL
# 2digit
# 1 or 2 alphabet
# 4 digit


from re import * 

vehicle_number=input(" enter number ")

rule="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}(-)?"

matcher=fullmatch(rule,vehicle_number)

print("invalid" if matcher==None else "valid")