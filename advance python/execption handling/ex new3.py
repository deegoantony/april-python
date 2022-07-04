#how to identified the exception:not the code error
a=[1,2,3,4]
i=int(input("enter a index"))
try:
    print(a[i])
except Exception as e:
    print("out of index",e)

n1=int(input("enter number 1"))
n2=int(input("enter number2"))
try:
    print(n1/n2)
except Exception as e:
    print("error",e)

