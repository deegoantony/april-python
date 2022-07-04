#monday:Encapsulation and abstraction

#encapsulation:it is wrapping of data...(wrapping up menas combining variables and methods in a single place is called encapsulation)
#how we can achive encapzulation : restricting the 'scope' of varibales and methods in the particular class
#scope is two type:public and private..defalt access specifer is public
class Encap:
    a=10 #one variable
    def setvalue(self): #one methode
        print("welcome")
# in here we are not spcifing any scope so scope of "a" and "setvalue" are public, that means these two can be used any where in the program(with in the class or out side the class)
# if we make the scope of varaibles and method as 'private' we will restrict it inside the calss it self can't use out side the class
#how can we change the scope in to private?
#__a=10,def __setvalue(self):
class Encap:
    a=10
    def setvalue(self):
        print("welcome")
ob=Encap()
ob.setvalue()
print(ob.a)
# now i am going to make it private
class Encap:
    __a=10 #private variable
    def setvalue(self):
        print("welcome")
ob=Encap()
ob.setvalue()
#print(ob.a)# it will shows an error becouse it is cout side the class

class Encap:
    __a=10 #private variable
    def setvalue(self):
        print("welcome")
        print(Encap.__a)
ob=Encap()
ob.setvalue()


# we can use anothen method called name mangling:(_classname__privatevariable)

