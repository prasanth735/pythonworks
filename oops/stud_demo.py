class Student:

    rollno:int
    name:str
    cource:str


    def set_stud(self,rollno,name,course):

        self.rollno=rollno
        self.name=name
        self.cource=course

    def display_stud(self):
        print(self.rollno,self.name,self.cource)



stud1= Student()
stud1.set_stud(11,"mammu","python")


stud2=Student()
stud2.set_stud(12,"suhail","python")

stud3=Student()
stud3.set_stud(13,"prasanth","python")


stud1.display_stud()                                                 
stud2.display_stud()                                                 
stud3.display_stud()                                                 



