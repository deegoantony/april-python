class Ide:
    def functionalites(self):
        funct=["read","write","append"]
        return funct
class Pycharm(Ide):
    def functionalites(self):
        funct=super().functionalites()
        funct.append("pop")
        funct.append("remove")
        return funct
class Vcs(Ide):
    def functionalites(self):
        fun=super().functionalites()
        fun.append("edit")
        return fun
ob=Pycharm()
print(ob.functionalites())
vsc=Vcs()
print(vsc.functionalites())