#age<50 location=india fnmae,lname,age,prof

f=open("C:/Users/MY PC/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    if((data[3]>'50') and (data[-1]=='india')):
        print(data[1:5])
        
