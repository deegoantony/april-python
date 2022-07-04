#1
lst=[i for i in range(1,1001) if i%7==0]
print(lst)

#2
lst=[i for i in range(1,10001) if '3' in str(i)]
print(lst)

#3
str='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
lst=[i for i in str if i==' ']
print(len(lst))