# remove special charector
f=open("new12","r")
spec='!@#$%^&*()_+'
st=''
dic={}
for i in f:
    data=i.rstrip("\n")
    for j in data:
        if j not in spec:
            st+=j
print(st)
#form this find the word count
data=st.split(" ")
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
fin_max=max(dic,key=dic.get)
print("most frequent word:", fin_max)







