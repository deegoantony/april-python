#find the highest mark print fname

lst=[('arjun',45),('vinay',35),('vipin',56),('amal',65)]
lst1=[]
for i in max(lst):
    lst1.append(i)
print("highest marked student is:",lst1[0])

#   or
for i in lst:
    lst1.append(i[1])

maxinum=max(lst1)
for j in lst:
    if j[1]==maxinum:
        print(j[0])




