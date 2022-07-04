cost=int(input("enter the cost of the bike in (RS):"))
if(cost>100000):
    print("you have road tax of 15% :",cost*0.15)
elif(100000>=cost>50000):
    print("you have  road tax of 10% :",cost*0.10)
else:
    print("you have road tax of 5% :",cost*0.05)