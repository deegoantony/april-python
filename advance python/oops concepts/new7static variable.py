#static varible:

#class:luminar
#name,roll,age,institution name,fees

class Luminar:
    institution_name="luminar techolab" #static variable
    fees=27000                          #static variable
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,Luminar.institution_name,Luminar.fees)
lum=Luminar()
lum.setvalue("deego",21,27)
lum.printvalue()

lum1=Luminar()
lum1.setvalue("arun",24,27)
lum1.printvalue()
