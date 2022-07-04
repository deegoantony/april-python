#read operation

f=open("sample 1","r")
for i in f:
    print(i)

#if bouthe the file are in same package
#f=open("sample 1")
#for windows use this"/"
f=open("C:\Users\MY PC\PycharmProjects\april_python\file operation\sample 1") #for linex
f=open("C:/Users/MY PC/PycharmProjects/april_python/file operation/sample 1")# for windows
for i in f:
    print(i)

