#21/12/23

# strings with same  length


# st1="ABC"
# st2="PQR"


# result=""


# for i in range(0,len(st1)):
#     out=st1[i] + st2[i]
#     result+=out

# print(result)
     


#------------------------------------------------------------------------------------------------------------------------------------------



#deferent length strings

st1=input("enter string1")
st2=input("enter string2")

small_len=min(len(st1),len(st2))
result=""


for i in range(0,small_len):
    out=st1[i] + st2[i]
    result+=out

if len(st1)>len(st2):
    rem=st1[small_len:]

else:
    rem=st2[small_len:]

result+=rem
print(result)

