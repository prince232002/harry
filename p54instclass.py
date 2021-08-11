
class Employee:
    no_of_leaves = 8 #property of class 
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
rohan.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)
print(rohan.__dict__)
print(rohan.no_of_leaves)

# here if we change rohan.no_of_employee
# print(rohan.no_of_leaves)
"""then it wil not print 8 not 9 only for rohan it will print 9 becoz no of
 leaves is shared by employee to its objects i.e, rohan and harry and it is 
 property of class employee so it can be changed by employee ( as class namespaces) -
 employee.no_of_leaves
print(Employee.no_of_leaves)
 """
