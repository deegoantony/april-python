class Student:
    def __init__(self,name,age,plc):
        self.name=name
        self.age=age
        self.plc=plc

    def printvalue(self):
        print(self.name,self.age,self.plc)
f=open("student","r")
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    plc=data[2]
    ob=Student(name,age,plc)
    ob.printvalue()

