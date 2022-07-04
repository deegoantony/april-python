#read number from the list
# print pair of number from the list
lst=[4,3,2,1]
sum=int(input("enter the sum value"))
for i in lst:
    for j in lst:
        if(i+j==sum):
            print("(",i,j,")")

#or
lst=[4,3,2,1]
element=int(input("enter the element"))
low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==element):
        print("pair number",lst[low],lst[upp])
        break
    elif(data>element):
        upp=upp-1
    else:
        low=low+1