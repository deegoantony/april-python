#class Person:name,age
#class Parent:place,phno
#class EMPLOY:id,desig,salary

class Person:
    def setvaluea(self,name,age): # 'self' also use 'this'
        self.name=name
        self.age=age

class Parent:
    def setvalueb(self,place,phno):
        self.place=place
        self.phno=phno
class Employ(Person,Parent):
    def setvaluec(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
        print(self.name,self.age,self.place,self.phno,self.id,self.desig,self.salary)
de=Employ()
de.setvaluea("deego",27)
de.setvalueb("kochi",8848102030)
de.setvaluec(101,"engineer",20000)