f=open("numbers","r")
lst=[]
for i in f:
    lst.append(int(i.rstrip("\n"))) #int used for convert it in to intigers
print(lst)
print(sum(lst))
#\n coming with the anwser

#to remove this "rstrip" function

#eg
line="hello\n"

data=line.rstrip("\n")
print(data) #"hello"