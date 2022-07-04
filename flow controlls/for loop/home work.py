# low
#upper
# prime number in between low and upp
low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

for num in range(low,upp+1):
    if (num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
             print(num)




