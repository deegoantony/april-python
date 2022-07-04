class Customer:
    def __init__(self,id,name,fname,age,prof,loc):
        self.id=id
        self.name=name
        self.fname=fname
        self.age=age
        self.prof=prof
        self.loc=loc
    def printdata(self):
        print(self.id,self.name,self.fname,self.age,self.prof,self.loc)
f=open("C:/Users/MY PC/Downloads/customer","r")
lst=[]
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    fname=data[2]
    age=data[3]
    prof=data[4]
    loc=data[-1]
    ob=Customer(id,name,fname,age,prof,loc)
    ob.printdata() #or print(ob.fname)
    #to uppend name,fanme,age,pro
    lst.append((ob.name,ob.fname,ob.age,ob.prof))
print(lst)



