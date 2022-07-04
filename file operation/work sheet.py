f=open("C:/Users/MY PC/Downloads/temper","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    dic.append(data)
    print(data)





