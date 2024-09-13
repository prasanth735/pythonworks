tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"

tt=tweets.split(" ")
count=0
for w in tt:
    if w.startswith("@"):
        count+=1
        print(w)
print(count)


     
   