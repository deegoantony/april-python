# eg of over riding

class C:
    def printa(self):
        print("inside 1")
    def printa(self):
        print("inside 2")
ob=C()
ob.printa()