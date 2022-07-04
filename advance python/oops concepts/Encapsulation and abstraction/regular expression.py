#regular  expression

#is a python pakage(pakage menas collection of module)

#regular  expression used for pattern matching

#here we using 'string' for pattern matching

#in here useing validation

#eg

import re
s="abaaabbbabaaaabab"
#finditer

#finditer(argument1,argument2)

#argument1:find_pattern

#argument2: string name
#find the 'ab' from 's'

import re
s="abaaabbbabaaaabab"
count=0
matcher=re.finditer('ab',s)

for i in matcher:
    count+=1
    print(i.start())# for finding the index oder comes in "ab" pattern
    print(i.group())# here we can find the 'ab' group
print(count)

#for probles in every topic go to www.hacker rank.com