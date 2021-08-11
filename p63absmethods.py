#abstract methods- or method without body
"""a abstract methods is a methods whose action is redefined in the 
child classes as per requirement of the object 
we can declare a methods as abstract method by using 
@abstractmethod decorator 
ex--
from abc import ABC , abstractmethod
Class Father(ABC):
     @abstractmethod
     def disp(self):
         pass
"""
#concrete methods__or method with body
"""
its a method whose action is defined in the abstract class itself 
Class Father(ABC):
    def disp(self):
        print("concrete methods")
"""
#you cant make the object of the abstract class only by creating its child inheritance
#PVM cant create objects of an abstract class
# its not neccessary to declare all methods abstract in a abstract class 
# abstract class have abstract methods and concrete methods
# If there is any abstract method in a class that class must be abstract 
# The abstract methods of an abstract class must be defined in its child class/subclass 
# if you inheriting any abstract class that have abstract method you must either provide 
#either provide implementation of method or make this class abstract  

"""when we use abstract class--
 when we have some common features in the abstract class 
 for their child classes which inherit it 
 """
from abc import ABC ,abstractmethod
class father (ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("concrete methods")

class child(father):
    def disp(self):
        print("child class")
        print("defining abstract methods")

c=child()
c.disp()
c.show()

# below is the ex showing the use of abstract class that have some feature i.e, gun and 
# area as different 

from abc import ABC ,abstractmethod
class defenceforce (ABC):
    @abstractmethod
    def area (self):
        pass
    def gun(self):
        print("gun= AK47")

class army(defenceforce):
    def area (self):
        print("army area = land")

class airforce (defenceforce):
    def area(self):
        print("airforce area= sky")

class navy(defenceforce):
    def area(self):
        print("navy area = sea")
 
a=army()
af=airforce()
n=navy()
a.gun()
a.area()
af.gun()
af.area()
n.gun()
n.area()