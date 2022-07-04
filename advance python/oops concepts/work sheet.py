#class Person:name,age
#class Parent:place,phno
#class EMPLOY:id,desig,salary

class Person:
    def setA(self,name,age):
        self.name=name
        self.age=age
class Parent(Person):
    def setB(self,place,phno):
        self.place=place
        self.phno=phno
class Employ(Parent):
    def setC(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
        print(self.name,self.age,self.place,self.phno,self.id,self.desig,self.salary)
ob=Employ()
ob.setA("Deego",27)
ob.setB("kochi",8848102030)
ob.setC(101,"engineer",20000)