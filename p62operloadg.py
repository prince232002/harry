#
# a = '5'
# b = '6'
#
# print(a + b)
#behind it works when we add operand
# print(str.__add__(a,b))
#__add__,__sub__,__mul__,__div__
class Student:
    def __init__(self,m1,m2): 
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return  s3

    def __gt__(self, other):  # gt- greater than ge- greater than and equal to 
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format( self.m1,self.m2)
# its a format to print string 

s1 = Student(58,69)
s2 = Student(69,65)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a)
#actually it call the __str__ method behind the seen
print(a.__str__())

print(s2)
#similar it call __str__() method behind the seen 
print(s2.__str__())

"""
Operator Overloading ---
-->means giving extended meaning beyond their predefined operational meaning. 
For example operator + is used to add two integers as well as join two strings 
and merge two lists. It is achievable because ‘+’ operator is overloaded by int class
and  str class. You might have noticed that the same built-in operator or function 
shows  different behavior for objects of different classes, this is called Operator 
Overloading.  
"""