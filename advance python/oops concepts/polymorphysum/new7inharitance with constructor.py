#inharitance with constructor

class Person:
    def __init__(self,name,age,plc):
        self.name=name
        self.age=age
        self.plc=plc
class Student(Person):
    def __init__(self,name,age,plc,rol,dep,clg):
        super().__init__(name,age,plc)
        self.rol=rol
        self.dep=dep
        self.clg=clg
    def printvalu(self):
        print(self.name,self.age,self.plc,self.rol,self.dep,self.clg)
ob=Student("deego",27,"kochi",101,"mech","kmp")
ob.printvalu()

