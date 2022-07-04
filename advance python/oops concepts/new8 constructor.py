#constructor==>to define instent variable in a object

class Person:
    def __init__(self,name,age,palce):
        self.name=name
        self.age=age
        self.place=palce
    def printvalue(self):
        print(self.name,self.age,self.place)
pe1=Person("deego",27,"kochi")
pe1.printvalue()

pe2=Person("anu",26,"kochi")
pe2.printvalue()