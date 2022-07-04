#lowe upper find the sum of even number and odd numbers
low=int(input("enter lower limit"))#3
upp=int(input("enter upper limit"))#10
even_sum=0
odd_sum=0
while(low<=upp):#3<=10
    if(low%2==0):#3%2not eqal
        even_sum+=low#(even_sum=even_sum+low)
    else:
        odd_sum+=low#3+0=3
    low+=1
print("sum of even number",even_sum)
print("sum of odd number",odd_sum)



