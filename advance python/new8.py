dic={"sedan":1500,"suv":2000,"pickup":2500,"minivan":2400,"semi":13600,"bicycle":7}

#print weight above 2000 collect the name ,name should be in uppercase

lst=[i.upper() for i in dic if dic[i]>2000]
print(lst)