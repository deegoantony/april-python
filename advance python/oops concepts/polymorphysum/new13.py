#calculate the sum
# def printvalue(*args):
#     print(sum(args))
# printvalue(1,2,5)

#or
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(3,4,5))
