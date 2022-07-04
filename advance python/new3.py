#list -comprehenssion

#empty-list 1 to 100

lst=[]

for i in range(1,101):

    lst.append(i)
print(lst)

#syntax of list comprehenssion

#lst=[print range]

lst=[i for i in range(1,101)]
print(lst)
#1 to 75
lst=[i for i in range(1,76,4)]
print(lst)

#1 to 100 even numbers

#lst=[print range condition]

lst=[i for i in range(1,101) if i%2==0]
print(lst)

#1 to 50 odd numbers
lst=[i for i in range(1,51) if i%2!=0]
print(lst)

#1 to 50 even
lst=[(i,"even") for i in range(1,51) if i%2==0]
print(lst)

#if more thene one condition

#syntax
#lst=[print if condition else condition print range]

# 3 conditions
# lst=[print1 if condition1 else print2 if condition2 else print3 range]

# 4 condition
# lst=[print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range]

# 1 to 50 if even square of the number,odd cube of the number
lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)

#1 to 50 if even square of the number,odd number
lst=[i**2 if i%2==0 else i for i in range(1,51)]
print(lst)

#1 to 50 if even square of the number,odd number (1,1),(2,4)...
lst=[(i,i**2) if i%2==0 else (i,i) for i in range(1,51)]
print(lst)

#if the number even print even or odd number with odd
lst=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,31)]
print(lst)