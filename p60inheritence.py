"""Different forms of Inheritance:
Single inheritance: When a child class inherits from only one parent class then it is called single inheritance.
#to use it we have the syntax __
# class_child(parent)
#here child is inheritance of parent so it have all its features
Multiple inheritance: When a child class inherits from multiple parent classes then it is called multiple inheritance
#to use multiple property like of parents mother and father we have syntax --
#class_child(A,B,..N)
Level inheritance : in this we define class by leveling
ex:
class A
class B(A)
class C(B)
#here class C has both the features of B and A """
#to use it we have the syntax __
# class_child(parent)
#here child is inheritance of parent so it have all its features
#to use multiple property like of parents mother and father we have syntax --
#class_child(A,B,..N)
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
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.no_of_holiday)

