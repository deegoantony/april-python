# read 3 num form console
# find the second largest number

#find the second largest number

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))

if(num1>num2)&(num1>num3):
    if(num2>num3):
       print("second largest is number 2",num2)
    else:
        print("second largest is number 3",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("second largest is number 1",num1)
    else:
        print("second largest is number 3",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("second largest is number 1",num1)
    else:
        print("second largest is number 2",num2)
else:
    print("invalid")