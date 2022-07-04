#multilevel inharitance

class A:
    def printa(self):
        print("inharitance A")
class B(A):
    def printb(self):
        print("inharitance B")
class C(B):
    def printc(self):
        print("inharitance C")
oc=C()
oc.printc()
oc.printb()
oc.printa()