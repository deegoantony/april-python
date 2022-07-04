#nested list
# to form a multiple list in a single list

lst=[[101,'arun','k',26,'bigdata',1000],
    [102,'amal','p',27,'python',1500],
    [103,'vishnu','e',24,'bigdata',1250],
    [104,'anoop','m',27,'python',2000],
    [105,'hari','r',25,'bigdata',1750],
    [106,'vinay','s',28,'bigdata',1500]]


print(lst)
#for saparate single lists

for i in lst:
    print(i)

#for finding name,lastname,age,prof

for i in lst:
    print(i[1],i[2],i[3],i[4])
#age above 25== 1st name,last name,age,prof,salary

for i in lst:
    if(i[3]>25):
        print(i[1],i[2],i[3],i[4],i[5])
