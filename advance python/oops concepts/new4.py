#class 'student'...name, roll num,department,college
class Student:
    def setvalue(self,name,roll_number,dep,clg):
        self.name=name
        self.roll_number=roll_number
        self.dep=dep
        self.clg=clg
    def printvalue(self):
        print(self.name)
        print(self.roll_number)
        print(self.dep)
        print(self.clg)
#object
pe1=Student()
pe1.setvalue("anu",5,"cs","kmp")
pe1.printvalue()

pe2=Student()
pe2.setvalue("ajith",7,"ec","kmp")
pe2.printvalue()

pe3=Student()
pe3.setvalue("jinu",8,"mech","kmp")
pe3.printvalue()