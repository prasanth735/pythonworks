# most freequent word

word="pneumonoultramicroscopicsilicovolcanoconiosis"
 
for w in word :
    count=max(word,key=lambda w:word.count(w)) 
    
print(count)
