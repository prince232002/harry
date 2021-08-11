# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")

  
# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)

"""  
remember that position of normal will be on the first it will not changable like 
we cant write like this :
funargs(*agrs,**kw,normal) #wrong produce error

*args parameter in a function definition allows the function to accept multiple arguments without knowing how many arguments. In other words it lets the function accept a variable number of arguments.

Datatype of args is tuple. Inside the function, you can access all the arguments passed as *args using a for loop. Or, you can use index to access the individual arguments. 
"""