#abstract class & abstract method
#abstract class:which have abstract methods
#abstract method:methods which having only declaration but not the definication
#concrete class :class without abstract method
from abc import ABC,abstractmethod
class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        pass
class Demo(AbstractDemo):#to make the class as concrete class overwrite all the method
    def display(self):
        print("Abstract Method")
#if the class is abstract class we can't creat an object for it
#object only can created in the concrete class
ob=Demo()
ob.display()
