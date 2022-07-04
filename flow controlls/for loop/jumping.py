#jumping statment

#break
#continue
#pass


#break
for i in range(1,51):
    if(i==25):
        break
    print(i)

#continue
for i in range(1,51):
    if(i==25): #1,2,...23,24,26,27....50
        continue
    print(i)

#pass
#means do nothing
for i in range(1,51):
    if(i==25):
        pass
    print(i)

#1-50 odd number square
for i in range(1,51):
    if(i%2==0):
        pass
    else:
        print(i**2)
