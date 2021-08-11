class Student:
    pass
"""pass- its a null statement . It is useful when you don't want to write the 
implementation of function but you want to implement it in the future """
# objects of class student -harry and rohan 
harry = Student()
larry = Student()
#these are the instances of the object
harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)

class abc:
    def func(self):
        print("fees")
abc.func(4)
#calling func using class 
c=abc()
c.func()


  
