from typing import Mapping


def printhar(string):
    return f"Ye string harry ko de de thakur {string}"

def add(num1, num2):
    return num1 + num2 + 5
 

print("aand the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)

"""remember _name_ ==_main_ 
only if you running the program from the same file not from amy 
any diff file by importing 
otherwise _name_ will print module name 
#if we write name = main then the code inside it can be access from the main file not other file 
# meant that other will import as module """