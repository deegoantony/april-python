#binarysearch

#lst=[7,4,3,1,2]

#1..sort the list(asending order)

#[1,2,3,4,7]

#2..declare 2 varyables

#low=0
#upp=len(lst)-1

#3...calculate the mid

#mid=(low+upp)//2 ....(0+4)//2=2

#then check 3 condition

#1 condition..search_element>lst[mid]...4>lst[2]=true

#low=mid+1

#2 condition ..search_element<lst[mid]...2<lst[mid]=true

#upp=mid-1

#3 condition...serach_element==lst[mid]...#3==3 element found

lst=[7,4,3,1,2]
num=int(input("eneter a number"))
lst.sort()
flag=0
low=0
upp=len(lst)-1
while(low<=upp):
    mid=(low+upp)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upp=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if(flag>0):
    print("number in the list")
else:
    print("number not in the list")