# suggestion

insta_users={"mohanlal","prithvi","dq","vijay","fahad","suresh gopi","lalu"}

mohan_lal_following={"prithvi","vijay","lalu"}

dq_following={"prithvi","fahad","suresh gopi","lalu"}

mohanlal_suggestion=insta_users.difference(mohan_lal_following)
mohanlal_suggestion.remove("mohanlal")
#print(mohanlal_suggestion)

#mutul friends

mutul=mohan_lal_following.intersection(dq_following)
#print(mutul)


order1={"cb","tika","fishfry","friedrice","vb","gheerost"}
order2={"cb","friedrice","nan","upuma","vegmeals","idly"}

# union_set=order1.union(order2)
# interset_order=order1.intersection(order2)
# new_order=union_set.difference(interset_order)

new_order=order1.symmetric_difference(order2)
# print(new_order)

st1={10,20,30}
st2={100,200,300}

st1.update(st2)
print(st1)