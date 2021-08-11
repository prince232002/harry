class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

class B:
    # def feature2(self):
    #     print("Feature 22 working")

    def __init__(self):
        # super().__init__()
        print("in B Init")

    def feature3(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

class C(B,A):

    def __init__(self):
        super().__init__()
        print("in C init")

    def feature2(self):
        print("Feature 222 working") #it not runs as super directly check in super class 
                                    #first then if not then it produces error not checks 
                                    # in subclass as here class C 
    def feat(self):
        super().feature2()


a1 = C()
a1.feat()

#here firstly it call as class B as superclass if there is no init then A as acc to
# method resolution order(mro) starts from L to R it prefer order B then A as  C(B,A) 
#so we got --> in B init
# super() -used to get intances of super class            
"""
-->sub class can access all features of super class but not vice-versa

--> If you create object of sub class it will first try find the init of sub class
if it is not found then it will call init of super class 

--> When you create object of sub class it will call init of sub class first if you
have call super then it will first call init of super class then call init of sub class 
"""
"""if class A and class B both has init constructor then print of B will print i.e "in B init"
on calling B() not print "in A init " if class B not have init then it calls the class A init and 
it print -- 
"in A init "
"""