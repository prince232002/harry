
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan = Employee()
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(rohan.printdetails()) 
harry = Employee("Harry", 255, "Instructor") #argument inside goes to the init calling
print(harry.salary)

#telusko
class computer:
     def __init__(self,cpu,ram): #argument are passing inside
         print("inti")
         self.cpu=cpu
         self.ram=ram

     def config(self):
         print("config is ",self.cpu,self.ram)
         #here we not pass cpu ie self.ram becoz cpu is not a local var its an object
         print("i5",16,'1tb')

com1=computer("i5",16)
com2=computer('i7',8)
#each time a object is created it will call init that it print init message twice 
com1.config()
com2.config()





"""types of methods__
1.instance methods 2.class methods 3.static methods 
special means it include underscore__
1.instance methods-
self-- it represents the instance of the class. That ,means for creating var we use 
and pass self i.e, instance methods
__init__(self)- represents contructors in class It use is to initialize value to the
object state
2.class methods- we use @classmethods
it is used to access class variable so it is bounded to class not the objects 
3.staticmethods-@staticmethods
it has nothing to do with class and intances variable
let we want to create factorial of a no then we can create using staticmethod

 """