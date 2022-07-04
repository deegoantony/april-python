#person [private]
#emloyee [person]

class Person:
    deego=10
    def setvalu(self,name,age):
        self.__name=name
        self.__age=age
    def pin(self):
        print(self.__name,self.__age)
class Employ(Person):
    def setvalue1(self,id,salary):
        self.id=id
        self.salary=salary
    def printvalue(self):
        print(self.__name,self.__age,self.id,self.salary)
ob=Employ()
ob.printvalue("deego",27,101,1000)
ob.setvalue1("101",1000)