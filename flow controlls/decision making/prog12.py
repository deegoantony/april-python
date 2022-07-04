sub1=int(input("enter subject 1 mark"))
sub2=int(input("enter subject 2 mark"))
sub3=int(input("enter subject 3 mark"))
sub4=int(input("enter subject 4 mark"))
sum=sub1+sub2+sub3+sub4
if(sum>=180):
    print("A+")
elif(179>=sum>=160):
    print("A")
elif(159>=sum>=140):
    print("B+")
elif(139>=sum>=120):
    print("B")
elif(119>=sum>=100):
    print("C+")
else:
    print("failed")