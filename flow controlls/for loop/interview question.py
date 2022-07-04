for i in "luminar":
    print(i)
#Q1
for num in range(-2,-5,-1):
    print(num,end=" ")
#Q2
x=0
for i in range(10):
    for j in range(-1,-10,-1):
        x+=1
print(x)

#Q3
for l in "john":
    if l=='0':
        pass
    print(l,end=" ")

#j o n
#j o h n

#Q4
x=0
a=0
b=-5
if(a>0):
    if(b<2):
        x=x+5
    elif(a>5):
        x=x+4
    else:
        x=x+3
else:
    x=x+2

#Q5
x=0
a=5
b=-5
if(a>0):
    if(b<0):
        x=x+5
    elif(a>5):
        x=x+4
    else:
        x=x+3
else:
    x=x+2

#Q6
a,b=12,5
if a+b:
    print("true")
else:
    print("false")

#if the value become zero it will  be false