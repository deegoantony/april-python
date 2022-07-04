# creat a calculater

#1..addition
#2..substraction
#3..multiplication
#4..division

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

print("press 1 for addition \npress 2 for substraction\npress 3 for multiplication\npress 4 for division")
choice=int(input("enter your choice"))
num1=int(input("enter number1"))
num2=int(input("enter number2"))
if(choice==1):
    add()
elif(choice==2):
    sub()
elif(choice==3):
    mul()
elif(choice==4):
    div()




