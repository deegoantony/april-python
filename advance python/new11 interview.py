#read a string from console remove wovels
dee='apple'
n=''
wov='aeiouAEIOU'
for i in dee:
    if i not in wov:
        n+=i
print(n)

