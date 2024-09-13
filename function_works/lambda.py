#cube
cube=lambda n:n**3

print(cube(3))

#+ve or -ve
num_chk=lambda num: "+ve" if num>0 else "-ve" if num<0 else "zero"

print(num_chk(5))

#largest number

max_num=lambda n1,n2: n1 if n1>n2 else n2
print(max_num(5,7))

#sum

add=lambda n1,n2: n1+n2

print(add(5,7)) 


#odd or even

od_evn=lambda n: "even" if n%2==0 else "odd"

print(od_evn(6)) 

#sorting words >>word length

text="good evening all"

words=text.split(" ")

srt_words=sorted(words,key=lambda w:len(w), reverse=True)
print(srt_words)






















