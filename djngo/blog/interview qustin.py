master_string="abbcddeghgggt"
chk_word="egg"
dic={}
str=""

for i in master_string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for u in chk_word:
    if u in dic:
        count=dic.get(u)
        if count>0:
            str+=u
        else:
            break
print(str==chk_word)
