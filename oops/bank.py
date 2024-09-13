

class Bank:

    ac_no=int
    name:str
    ac_type:str
    ifsc_code:str
    branch:str
    balance:str


    def create_ac(self,name,ac_no,ac_type,ifsc_code,branch,bal):
        self.ac_no=ac_no
        self.name=name
        self.ac_type=ac_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=bal

    def deposite(self,amt):
        self.balance+=amt
        print(f"your {self.ac_no} has been credited with Rs.{amt}. balance Rs.{self.balance}")

    def withdraw(self,amt):
        if amt>self.balance:
           print("insufficient balance")
        else:
           self.balance-=amt
           print(f"your {self.ac_no} has been debited with Rs.{amt} available balance is Rs.{self.balance}")

    def get_balance(self):
        print(f"your balance is Rs.{self.balance}")


bnk=Bank()

bnk.create_ac("abn",123,"current",1254,"nbr",0)
bnk.deposite(5000)
bnk.withdraw(2500)
bnk.get_balance()

