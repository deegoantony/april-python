#bigdata== age,fname,lname,salary
lst=[[101,'arun','k',26,'bigdata',1000],
    [102,'amal','p',27,'python',1500],
    [103,'vishnu','e',24,'bigdata',1250],
    [104,'anoop','m',27,'python',2000],
    [105,'hari','r',25,'bigdata',1750],
    [106,'vinay','s',28,'bigdata',1500]]
for i in lst:
    if(i[4]=='bigdata'):
        print(i[3],i[1],i[2],i[5])

#salary >1750 and age>25

for i in lst:
    if(i[5]>1750 and i[3]>25):

            print(i[1],i[2],i[4])
#total salary
sum=0
for i in lst:
    sum+=i[5]
print(sum)
