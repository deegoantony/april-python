# lst=[4,5,10,12,20]
#lst1=[47,46,41,39,31]

#logic...total sum of lst=51
#51-1st element,51-4=47
lst=[4,5,10,12,20]
lst1=[]
for i in lst:
    num=sum(lst)-i
    lst1.append(num)
print(lst1)

