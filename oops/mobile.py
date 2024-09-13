#13/12/2023

class Mobile:

    brand=str
    model:str
    price:int
    

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def dislpay_mobile(self):
        print(self.brand,self.model,self.price)


    def __str__(self):
        return self.brand
    

mob= Mobile("apple","xs",50000)
mob1= Mobile("samaung","s23ultra",120000)


mob.dislpay_mobile()
mob1.dislpay_mobile()


print(mob)
print(mob1)