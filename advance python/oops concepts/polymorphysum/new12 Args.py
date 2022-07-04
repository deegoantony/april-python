#*args

#2 numbers
# def printvalue(num1,num2):
#     print(num1,num2)
# printvalue(2,3,4) #3rd value will not work in this case

#to print multiple argument from user
def printvalue(*args): #not only the 'args' also can use any words
    print(args)
printvalue(5,5,7,8,9)

