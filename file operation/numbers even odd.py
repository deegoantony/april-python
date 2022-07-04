f=open("numbers","r")
lst=[]
even_lst=[]
odd_lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))

print(lst)
for i in lst:
    if(i%2==0):
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(even_lst)
print(odd_lst)
print("even sum=",sum(even_lst))
print("odd sum=",sum(odd_lst))
