text="123#pneumonoultramicroscopicsilicovolcanoconiosis"
print(len(text))

c_count=0

for ch in text:
         if ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u": # if ch not in ["a","e","i","o","u"]:
            if ch.isalpha():
               c_count+=1
print(f"constant count is {c_count}")