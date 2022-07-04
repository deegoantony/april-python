#find the element in the list or not
lst=[1,9,3,5,20,39,45]
num=int(input("enter a number"))
if num in lst:
    print("element found")
else:
    print("element is not found")

#OR
flg=0
for i in lst:
    if(i==num):
        flg=1
        break
if(flg>0):
    print("element found")
else:
    print("not found")

#leaner search
#it is time cosuming,to over come this problem we use binary search