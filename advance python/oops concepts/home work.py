#from the word count find the most frequent word

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
negativedic={}
positve='good'
negative='bad'
lst=[]
st=''
for i in f:
    data=i.rstrip("\n").split(" ")
    for j in data:
        if j not in lst:
            lst+=j
print(lst)
