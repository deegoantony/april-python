#development an algorithm
#name:sentiment analysis algorithm
# 1 word by word :tokenization
# two dictionary creation +,and-ve
# compare with +ve and -ve dic..
# if the value is +ve add=1
# if the value is -ve add=-1
# if the value is neutral add=0
# if the total value is +ve it is good

f=open("assignment","r")
positivedic={}
# negativedic={}
positve='good bad'
# negative='bad'
# lst=[]
st=''
for i in f:
    data=i.rstrip("\n")
    for j in data:
        if j in positve:
            st+=j
print(st)
data=st.split(" ")
for i in data:
    if i not in positivedic:
        positivedic[i]=1
    else:
        positivedic[i]+=1
print(positivedic)
print(positivedic['good'])
print(positivedic['bad'])
if (positivedic['good']>positivedic['bad']):
    print("is a positive comment")
elif (positivedic['good']==positivedic['bad']):
    print("the comment is neutral")
else:
    print("is a negative comment")








