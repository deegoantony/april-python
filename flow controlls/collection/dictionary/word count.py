#word count

line='cat rat bus cat car cat bus car rat'
print(line)
#to convert line in to word by word data
data=line.split(" ") #space for seperation
print(data)
dic={}
for i in data: #cat,rat
    if i not in dic: #cat,rat
        dic[i]=1 #cat=1,rat=1
    else:
        dic[i]+=1
print(dic)



