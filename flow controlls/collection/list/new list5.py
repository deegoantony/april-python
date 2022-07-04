#to add a single elements in the list = we can use append function
lst=[]

#append
lst.append(10)
lst.append(50)
lst.append("bigdata")
print(lst)

#to add more than one function extend function used

#extend
lst.extend([60,70,80])
print(lst)

#insert
#to add element in a partiqular area of the list
#add 150 in 2nd position
lst.insert(1,150)
print(lst)

#5 position add 'bigdata'
lst.insert(4,'bigdata')
print(lst)

