#1 to 75 then creat even number list and odd number slist and calculate the sum

lst=[]
lst1=[]
lst2=[]

for i in range(1,76):
    lst.append(i)
print(lst)
for i in lst:
    if(i%2==0):
        lst1.append(i)
    else:
        lst2.append(i)

print(lst1)
print(lst2)
print(sum(lst))
print(sum(lst1))
print(sum(lst2))