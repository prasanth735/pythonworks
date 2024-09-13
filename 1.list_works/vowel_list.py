lst=["red","green","blue","white","black","apple","ignore","under"]


start_with_vowel=[word for word in lst if word[0] in["a","e","i","o","u"]]
print(start_with_vowel)

 
consonent=[word for word in lst if word[0] not in ["a","e","i","o","u"]]
print(consonent)





