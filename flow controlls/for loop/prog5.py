#low to upper even number
low=int(input("enter the lower limit"))
upp=int(input("enter the upper limit"))
for low in range(low,upp+1):
    if(low%2==0):
        print(low)