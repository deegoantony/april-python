num=int(input("ente the number"))
sum=0
while(num!=0):
    deg=num%10
    sum=(sum*10)+deg
    num=num//10
print(sum)