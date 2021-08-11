#constructor decide the memeroy for an object stores in heap memory 
class computer:
    def __init__(self):
        self.name='prince'
        self.age=25
    def update(self):
        self.age=38
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c2=computer()
# by using dot we access methods
c1.update()
c2.age=55
#here we are comparing c1 (self) with c2 (other)
if c1.compare(c2):
    print("they are same ")
else:
    print("they are differ")

print(c1.name,c1.age)
print(c2.name,c2.age)

