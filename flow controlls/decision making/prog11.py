#largest amoung 3 numbers

num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
if(num1>num2)&(num1>num3):
    print("number 1 is largest",num1)
elif(num2>num1)&(num2>num3):
    print("number 2 is largest",num2)
else:
    print("number 3 is largest",num3)

