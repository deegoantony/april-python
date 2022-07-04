employ=['vinay','anu']
default={"designation":"bigdata","salary":1000}

#{'vinay':{"designation":"bigdata","salary":1000},'anu':{"designation":"bigdata","salary":1000}}
# dic={}
# for i in employ:
#     dic[i]=default
# print(dic)

#or
#fromkeys : it return a dictionary with specified key with specifed values
res=dict.fromkeys(employ,default)
print(res)

print(res['vinay'])
