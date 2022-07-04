#multiple inharitance:==> child will inharit more than one parent

class A:
    def printa(self):
        print("inharitance A")
class B:
    def printb(self):
        print("inharitance B")
class C(A,B):
    def printc(self):
        print("inharitance C")
oc=C()
oc.printc()
oc.printb()
oc.printa()