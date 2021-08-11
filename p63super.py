class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        self.special = "Special33sql"

        print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)

"""
first if we calls b.classvar1 then firstly it checks in the instance of init of A if 
it is not there then it checks in class B it not there then it checks in superclass A


super()--
it let you avoid referring to the base class explicitly
"""