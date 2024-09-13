# text="cricket,update,pakistan,won by,80,runs,against,netherland"
# words=text.split(",")

# for w in words:
#     print(w)

#===========================================================================================================================================

text="pneumonoultramicroscopicsilicovolcanoconiosis"
print(len(text))


v_count=0
for ch in text:
    if ch in["a","e","i","o","u"]:# >>>> vowel count
    # if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u": >>> vowel count
        v_count+=1

print(f"vowel  count is {v_count}")

