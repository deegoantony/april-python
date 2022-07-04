#reverse
#1234..4321
num=int(input("enter a number")) #135
res=0
while(num!=0): #135!=0,13!=0
    dig=num%10 #135%10=5,13%10=3
    res=(res*10)+dig #(0*10)+5=5,(5*10)+3=53
    num=num//10 #135//10=13,13//10=1
print(res)

