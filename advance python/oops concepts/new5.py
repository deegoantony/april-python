#class 'employ==empyname,desig,salary,company
#creat 3 employ data
class Employ:
    def setvalue(self,empyname,desig,sal,cmpy):
        self.empyname=empyname
        self.desig=desig
        self.sal=sal
        self.cmpy=cmpy
    def printvalue(self):
        print(self.empyname)
        print(self.desig)
        print(self.sal)
        print(self.cmpy)
pe1=Employ()
pe1.setvalue("arun","manager",30000,"benix")
pe1.printvalue()