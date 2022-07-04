#find the maximum tem in each district
f=open("C:/Users/MY PC/Downloads/temper","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    dis=data[0]
    tem=int(data[1])
    if dis not in dic:
        dic[dis]=tem
    else:
        (old_tem)=dic[dis]
        if tem>old_tem:
            dic[dis]=tem
print(dic)











        #
        # if (old_tem>tem):
        #     print(dic,old_tem)
        # else:
        #     print(dic,tem)





