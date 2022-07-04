#over rinding
#METHODE name same and number of argument same
#child class will over wirte parent class


class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside class A",self.num1+self.num2)
class Add2(Add):

    def sum(self,nu1,nu2):
        self.nu1=nu1
        self.nu2=nu2
        print("inside class B",self.nu1+self.nu2)
ob=Add2()
ob.sum(2,4)