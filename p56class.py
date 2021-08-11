
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves
        # return cls.no_of_leaves


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Harry", 255, "student")

rohan.change_leaves(34)
print(Employee.no_of_leaves)

#class methods are bounded to class not the objects of the class 
#it access class variable not instance variable 