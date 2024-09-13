f=open("C:\\Users\\user\\Desktop\\my python\\fileio\\news.txt","r")

# count=0
# for line in f:
#     words=line.rstrip("\n").split(" ")
#     count=count+len(words)
#     # print(words)
# print(count)

# total number of words


word_count={}

for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w in word_count:
            word_count[w]+=1
        else:
            word_count[w]=1
print(word_count)