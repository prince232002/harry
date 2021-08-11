'''
#method overloading--

--> Not all program'g supports this but python does. 

--> If want to define a function in such a way that there are multiple way to call it 
Means we can decides to pass number of parameter ourselves i.e, zero,one,two or atmost 
maximum parameter that has been mentioned while defining the method 
as shown in below ex--

'''
                         #(--method overloading--)

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):

        s = 0

        if a!=None and b!=None and c!=None:
          s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a

        return s


s1 = Student(58,69)

print(s1.sum())



                        #(---Method Overriding---)

class A:

    def show(self):
        print("in A Show")

class B(A):

    def show(self):
        print("in B Show")


a1 = B()
a1.show()
#method overiding-if two classed have same methods names as well as parameters
"""if my father have phone let nokia445 then if someone ask me which phone i have then 
i used to say that i have nokia but now I have minote9 so if someone ask me then i 
dont say that i have nokia 445 instead i would say i have minote9 that's how overwriting 
works
ex : as in above----------
if we pass simple in class B(A) then call show() it will call for show() in class A and 
it print -->in A show       ,as it dont have show()
but if we declare show() inside classB(A) then now it print --> in B show 
as now it have its own method that is overwritten  i.e, overiding 
"""