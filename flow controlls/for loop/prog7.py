#low upp add even or odd sum
low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
even_sum=0
odd_sum=0
for i in range(low,upp+1):
     if(i%2==0):
      even_sum+=low
     else:
       odd_sum+=low
print("odd sum",odd_sum)
print("even sum",even_sum)