f=open("C:/Users/MY PC/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    #for printiong fname,lastname,age
    #print(data[1],data[2],data[3])

    #split methode
    #print(data[1:4])
#age<50 fname,lname,age,profe
    if(data[3]>'50'):
        print(data[1],",",data[2],",",data[3],",",data[4])