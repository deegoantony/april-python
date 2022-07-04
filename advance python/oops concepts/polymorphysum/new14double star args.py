#**args
#keard :key_word argument
#data into dictionary key :value

# def printvalue(*args):
#     return args
# print(printvalue(101,"vinay","k",26,"bigdata",1000))
#101:empno
#vinay:fname
#k:last_name
#26:age
#bigdata:prof
#1000:salary

def printvalue(**args):
    return args
print(printvalue(empid=101,fname="vinay",lname="k",age=26,prof="bigdata",sala=1000))