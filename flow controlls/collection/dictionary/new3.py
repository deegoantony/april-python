#print the key -value in to coloumn
dic={"roll":101,"name":'vinay',"age":26,"dep":'bigdata',"salary":10000}
for i in dic:
    print(i,",",dic[i])

#to age 26 to== 36

dic["age"]+=10
print(dic)

#to add new key:value

dic['total']=150
print(dic)

#to delete a key :value

del dic['age']
print(dic)

#applying "in" for true or falls

dic={"roll":101,"name":'vinay',"age":26,"dep":'bigdata',"salary":10000}
print('name' in dic)  #true