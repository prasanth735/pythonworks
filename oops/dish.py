class Cuisine:
    name=str

    def __init__(self,name):
        self.name=name
        

    def   __str__(self):
        return self.name

class Dish(Cuisine):
    ingrediance=str
    price=int

    def __init__(self, name,ingrediance,price):
        super().__init__(name)
        self.ingrediance=ingrediance
        self.price=price

    
dis=Dish("lime","lemon,water,suger",20)
print(dis)
    


