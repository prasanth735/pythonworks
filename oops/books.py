class Book:
    name:str
    author:str
    pages:int
    price:int


    def __init__(self,name,author,pages,price):
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display_book(self):
        print(self.name,self.author)

    def __str__(self):
        return self.name


bk= Book("randamoozham","mt",489,658)
bk1= Book("aadujeevitham","benyamin",500,550)

bk.display_book()
bk1.display_book()


print(bk)