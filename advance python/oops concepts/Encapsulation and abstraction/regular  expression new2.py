#basic rules in regular experssion

import re
counr=0
rule='[abc]'
matcher=re.finditer(rule,'abc @sabir123')

for i in matcher:
    counr+=1
    print(i.group())
    print(i.start())
print(counr)
#if we want execpt abc use this symbol'^'

import re
counr=0
rule='[^abc]'# here execpt abc
matcher=re.finditer(rule,'abc @sabir123')

for i in matcher:
    counr+=1
    print(i.group())
    print(i.start())
print(counr)
#to finding A-Z

import re
counr=0
rule='[A-Z]'#here '-' used for A,B,...X,Y,Z
matcher=re.finditer(rule,'abc @sabir123')

for i in matcher:
    counr+=1
    print(i.group())
    print(i.start())
print(counr)
