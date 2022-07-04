f=open("paragraph","r")
dic={}

for i in f:
    data=i.rstrip("\n").split(" ")
    print(data)
    for i in data:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
print(dic)
for i in dic:# for words in coloum
    print(i,dic[i])

    #or
for k,v in dic.items(): #items used for print key value pair
    print(k,",",v)