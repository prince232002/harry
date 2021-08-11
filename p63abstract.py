"""Abstraction-
By default, Python does not provide abstract classes. Python comes with a module that
 provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
  ABC works by decorating methods of the base class as abstract and then registering 
  concrete classes as implementations of the abstract base. A method becomes abstract 
  when decorated with the keyword @abstractmethod.
Abstract class have atleast 1 abstract methods and we dont define them and it is declared 
but contain no implementation 
"""
"""Implementation Through Subclassing : 
By subclassing directly from the base, we can avoid the need to register the class explicitly. In this case, the Python class management is used to recognize PluginImplementation as implementing the abstract PluginBase. so we need declare 
methods in parent class to subclass.
"""

# Python program showing
# implementation of abstract
# class through subclassing
 
import abc
 
class parent:      
    def geeks(self):
        pass
 
class child(parent):
    def geeks(self):
        print("child class")
 
# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))