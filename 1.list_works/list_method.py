orders=["friedrice","gheeroast","vb","cb","bb","aaa","aaa","aaa"]
#           0           1         2    3   4     5     6     7
#           -8         -7        -6   -5  -4    -3    -2    -1

orders.append("tea") # adding object to the list >>> only one >>> addind to last position
print(orders)

print(orders.count("aaa")) # count the specified object

print(orders.index("bb"))

print(orders.pop(0)) # remove object >> defult value of pop= -1>>> last poosition

orders.insert(1,"goby") # insert object to the specified position

orders.remove("aaa") # remove object by name >>> first occurance will remove

print(orders)





mnj_favt_color=["yellow","white","black","green"]

# mbn_favt_color=mnj_favt_color.copy()
# mbn_favt_color.remove("black")

# print(mnj_favt_color)
# print(mbn_favt_color)

# mnj_favt_color.reverse()

mnj_favt_color.sort() #sort only list >>> sort>>> method in list

# print(mnj_favt_color)

word="mohammed"

for w in word:
    if w=="a":
        word.strip("a")

print(word)
