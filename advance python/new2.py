#map function
#   &
#filter function


#map....
#for ecah elements need corresponding value we use map

#filter...
#for surtaine elements needs value use filter

#syntax
#variable_name=list(map(argument,argument2))
#variable_name=list(filter(argument,argument2))

#argument1==>function
#argument2==>iterable

lst=[1,2,3,4,5,6,7,8,9,10]
def square(num):
    res=num**2
    return res
data=list(map(square,lst))
print(data)

#by using lambda
data=list(map(lambda num:num**2,lst))
print(data)

#filter

#def even(num):
#   return num%2==0

data=list(filter(lambda num:num%2==0,lst))
print(data)
#add 1 to element
lst=[1,2,3,4,5,6,7,8,9,10]

data=list(map(lambda num:num+1,lst))

print(data)