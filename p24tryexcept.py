print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
try:
    print("The sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)



print("This line is very important")

# try except : use for to handling a part of program .  
# try block used to check code for the error , try block will execute when there is no error in the program , except will execute when the code encounters an error . 
# except will print error as an string 
# for ex: while loading a website if your connection is weak then you see image is not opening or any input error but remaining content will open , that try except allowing to execute the remaining program 