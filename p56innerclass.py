"""to use inner class
object of the inner class always defines inside the outer class 
# in below - line 8 see 
to access  the inner class we use --
outerclass.innerclass()
"""
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap=self.laptop()
    
    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)
        
s1=student("Navin",3)
s2=student("jenny",5)

s1.show()
lp=student.laptop()

