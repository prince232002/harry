a = 9
b = 8
# c = sum((a, b)) # built in function

def function1(a, b):
    print("Hello you are in function 1", a+b)

def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    print(average)
    # return average
    # return will use when our function returns something if not use then it will return  none 
    # return is not used when there is no expression in our program
function2(4,4)
# v = function2(5, 7) #passing paramter and call function2
# print(v)
# print(function2.__doc__)

# docstring- it is the first line in the  function  that is written as comment inside triple quotes, but not read as comment as it will execute on cmd to remember some warning or suggestion

"""to print the return use print while calling the function and
to if you are using print in the function then just use call the function
"""