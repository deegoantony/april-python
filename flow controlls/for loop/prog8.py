# check given number is prime number or not
#2,3,5,7,11,13
#if 9 (2,8) range it will be divisible is number is not prime

num=int(input("ener a number"))
fag=0
for i in range(2,num):

    if(num%i==0):
        fag=1
        break
if(fag>0):
    print("not prime")
else:
    print("prime")


