#person:name,age
#child:plc,school
#stud:roll,depat,clg
# print:name,age,depat,clg

class Person:
    def seta(self,name,age):
        self.name=name
        self.age=age
class Child(Person):
    def setb(self,plc,sch):
        self.plc=plc
        self.sch=sch
class Stud(Child):
    def setc(self,roll,depat,clg):
        self.roll=roll
        self.depat=depat
        self.clg=clg
        print(self.name,self.age,self.depat,self.clg)
ob=Stud()
ob.seta("deego",27)
ob.setb("kochi","hss")
ob.setc(101,"mech","kmp")