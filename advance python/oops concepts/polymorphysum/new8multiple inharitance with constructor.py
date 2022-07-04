#multiple inharitance with constuctor

#person:name,age,plc
#employ:id,dep,salary
#student:roll,clg

class Person:
    def __init__(self,name,age,plc):
        self.name=name
        self.age=age
        self.plc=plc
class Employ:
    def __init__(self,id,dep,sal):
        self.id=id
        self.dep=dep
        self.sal=sal
class Student(Person,Employ):
    def __init__(self,roll,clg,name,age,plc,id,dep,sal):
        Person.__init__(self,name,age,plc)
        Employ.__init__(self,id,dep,sal)
        self.roll=roll
        self.clg=clg
    def printvalue(self):
        print(self.name,self.age,self.plc,self.id,self.dep,self.sal,self.roll,self.clg)
ob=Student("Deego",27,"kochi",101,"mech",2000,110,"kmp")
ob.printvalue()
