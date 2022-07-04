#find the 1st recursive element
pattern='ABCDBCDA' #B is the element
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print(i,"is the 1st recursive element")
        break