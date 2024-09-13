from abc import ABC,abstractmethod




class Dbconnect(ABC):

    @abstractmethod
    def __init__(self,user,password,port,database):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def exicute_query(self):
        pass

    @abstractmethod
    def close(self):
        pass


class Mydb(Dbconnect):

    def __init__(self, user, password, port, database):
        self.user=user
        self.password=password
        self.port=port
        self.database=database
   


    def connect(self):
        print("connect")


    def exicute_query(self):
        print("enter query")

    def close(self):
        print("close")



db=Mydb("prasanth",1234,45,"mydb")
db.connect()
db.exicute_query()
db.close()