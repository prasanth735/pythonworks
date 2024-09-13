#18/12/23



class Parent1():

    def m1(self):
        print("inside parent1 m1 method")


class Parent2( Parent1):
    def m2 (self):
        print("inside parent2 m2 method")

class Child(Parent2):
    def c(self):
        print("inside child c methhod")


ch=Child()
ch.c()
ch.m1()
ch.m2()
