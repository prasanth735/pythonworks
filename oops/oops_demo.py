class Employee:

    id:int
    name:str
    department:str
    salary:int

    def set_emp(self,id,name,dep,sal):

        self.id=id
        self.name=name
        self.department=dep
        self.salary=sal

    def display_emp(self):
        print(self.id,self.name,self.department,self.salary)





emp1=Employee()
emp1.set_emp(123,"ram","hr",50000)


emp2=Employee()
emp2.set_emp(456,"vijay","qa",55000)

emp3=Employee()

emp3.set_emp(159,"mammu","chaiwala",151)



emp1.display_emp()
emp2.display_emp()
emp3.display_emp()



