results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]


total=sum([res["A+"] for res in results])

print("hereeee",total)
#1..win % of tvm
for result in results:
    if result["district"]=="tvm":
        print(result["win"])
print([i["win"] for i in results if i["district"]=="tvm"])
#1..by using list comprehences
tvm_win=[result["win"] for result in results if result["district"]=="tvm"]
print(tvm_win)

#2.. sort by using win %

results.sort(key=lambda i:i["win"],reverse=True)
print(results)

#3..highest win%
print(max(results,key=lambda res:res["win"]))

#4..district with lowest win %:
print(min(results,key=lambda i:i["win"]))

#4 dis with high A+:
print(max(results,key=lambda i:i["A+"]))

#5 dis with low A+:
print(min(results,key=lambda i:i["A+"]))

#total number of A+:
sum=0
for i in results:
    sum+=i["A+"]
print("total number of A+ is:",sum)
#  or


#total win %:
sum=0
for i in results:
    sum+=i["win"]
print("total win % is:",sum/10,"%")