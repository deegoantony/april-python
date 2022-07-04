#7.none of the above
#9.#
#10.none of these
#11.a**b
#12.D
#14.B
#15.C
#17.D
#18.D
#19.B
#20.B
#21.A
#22.A
#23.C
#24.D
#3

for num in range(0,101):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)