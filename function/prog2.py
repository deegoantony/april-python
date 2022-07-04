#find the cube of a number

def add():
    num=int(input("enter a number"))
    sum=num**3
    print(sum)
add()

def add(num):
    sum=num**3
    print(sum)
add(2)

def add(num):
    sum=num**3
    return sum
data=add(2)

print(data)