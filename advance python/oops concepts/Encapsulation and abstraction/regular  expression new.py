import re
s="addfeadghraddjiadaghad"
count=0
matcher=re.finditer('ad',s)
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)