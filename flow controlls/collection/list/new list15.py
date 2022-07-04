#list slicing
lst=[10,20,35,67,47,89,56,80]

#index

print(lst[1:4])  #lst[1],lst[2],lst[3]
print(lst[3:7])  #lst[3],lst[4],lst[5],lst[6]
print(lst[:5])   #lst[0],lst[1],lst[2],,,,lst[4]
print(lst[3:])   #lst[3], to end of the list
print(lst[:])  #print all the elements in the list

#negative index

#[-1 to -n]

print(lst[-1])  #80
print(lst[-3])  #89

print(lst[-4:-1])  #lst[-4],lst[-3],lst[-2]
print(lst[-2:-5])  #not posible
print(lst[-3:])   #-3,-2,-1
print(lst[:-4])  #start to -5