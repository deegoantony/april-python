clas=int(input("total number of cls held"))
attendence=int(input("number of class attended"))
sum=(attendence/clas)*100
print(sum)
if(sum>75):
    print("he is eligible")
else:
    print("he is not eligible")