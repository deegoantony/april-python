#methode over riding

class A:
    def printa(self):
        print("inside class A")
class B(A):
    def printa(self):
        print("inside class B")
class C(B):
    def printa(self):
        print("inside class C")
ob=C()
ob.printa()