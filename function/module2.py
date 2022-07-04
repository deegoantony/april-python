#syntax

#import packagename.modulename
#varibalename=packagename.modulename.fncall

import function.module1
data=function.module1.add(10,20)
print(data)

data1=function.module1.sub(20,10)
print(data1)

data2=function.module1.mul(20,30)
print(data2)

data3=function.module1.div(30,10)
print(data3)

#simple methode

#without passing package name and module repeatedly

from function.module1 import *
data=add(30,20)
print(data)

data1=sub(30,20)
print(data1)

data2=mul(30,20)
print(data2)

data3=div(30,10)
print(data3)