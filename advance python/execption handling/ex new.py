#exceptional handling
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

#print(num1/num2) #3/0== error

#exceptional handling==>to handle unexpected error from the input.we use execption handling
# 3 blocks

# 1..try block:add the try block when it will be an error
# 2..except block:to add solution
# 3..finally:similar to the pass

try:
    print(num1/num2)
except:
    print("zero division error")
finally:
    print("nothing")