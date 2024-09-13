# 20/12/2023



from abc import ABC,abstractmethod



class Car(ABC):

    @abstractmethod
    def __init__(self,name,brand,model):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accilerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass





class Swift(Car):


    def __init__(self, name, brand, model):
        self.name=name
        self.brand=brand
        self.model=model

    def start(self):
        print("swift start")


    def accilerate(self):
        print("swift runs")


    def stop(self):
        print("swift stop")




c1=Swift("swift sports","suzuki","2023")

c1.start()
c1.accilerate()
c1.stop()