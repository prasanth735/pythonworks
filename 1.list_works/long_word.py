items=["ball","bat","stumps","helmet","arc","cricketball"]


max_word=items[0]

for i in range(1,len(items)):
    current_word=items[i]
    if len(current_word)> len(max_word):
        max_word=current_word
print(max_word)



