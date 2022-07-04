#name,age,prof,salary
dic={"name":'deego',"age":27,"prof":'python',"salary":10000}
print(dic)
#name to 1st name
dic["fname"]=dic["name"]
del dic["name"]
print(dic)

#prit profession
print(dic["prof"])

#find company
print("company" in dic)

#add company =luminar
dic["company"]='luminar'
print(dic)

#salary+5000
dic['salary']+=5000
print(dic)

#key : value pair print
for i in dic:
    print(i,",",dic[i])
