def add():
    add=num1+num2
    print(add)
def sub():
    sub=num1-num2
    print(sub)
def mul():
    mul=num1*num2
    print(mul)
def div():
    div=num1/num2
    print(div)
print("number 1 for addiction \n number 2 for substraction \n number 3 for multiplication \n number 4 for division")
choice=int(input("enter your choice"))
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
if(choice==1):
    add()
elif(choice==2):
    sub()
elif(choice==3):
    mul()
elif(choice==4):
    div()
