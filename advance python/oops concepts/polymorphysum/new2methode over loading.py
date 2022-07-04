#methode over loading:same methode name and different number of 'arguments'
#python does't suppor methode over loading

class A:
    def suma(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class B(A):
    def suma(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)
ob=B()
ob.suma(1,6) #will not work
ob.suma(4,5,6) #will work