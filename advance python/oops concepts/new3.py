class Person:
    def setvalue(self,name,age,place): #argumnet to instance argument self used, for used in another argument
        self.name=name  #change the argument 'name' into instance argument
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
pe1=Person() #object
pe1.setvalue("anu",38,"kochi")
pe1.printvalue()

pe2=Person()
pe2.setvalue("deego",27,"kochi")
pe2.printvalue()