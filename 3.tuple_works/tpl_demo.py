# tuple
#define ()
# insertion order >> preserved
# duplicate >> allowed
# mutable >> not possible
# method 2


tp=(10,20,30,40,30,20)
print(tp)

# tp[0]=100  >>> not possible
# print(tp[0])

color1=("red",) # ,
color=("red")
print(type(color))
print(type(color1))


# methods  

print(tp.count(20))
print(tp.index(10))