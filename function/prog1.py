#factorial 3,..3*2*1=6

def add():
    num=int(input("enter a number"))
    sum=1
    for i in range(1,num+1):
        sum*=i
    print(sum)
add()

def add(num):
    sum=1
    for i in range(1,num+1):
        sum*=i
    print(sum)
add(3)

def add(num):
    sum=1
    for i in range(1,num+1):
        sum*=i
    return sum
data=add(3)
print(data)