# 1st class Person,:name,age,place
# 2nd class Student:roll,dep

class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Student(Person):
    def printvalue(self,roll,dep):
        self.roll=roll
        self.dep=dep
        print(self.name,self.age,self.place,self.roll,self.dep)
va=Student()
va.setvalue("deego",27,"kochi")
va.printvalue(21,"mech")