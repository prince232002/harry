"""
Duck typing --
if there is a bird which behaves like a duck ,walk like a duck and quack
like a duck then its a duck

example-
in the above ex we see that we have the method execute 
it doesnt matter we pass class Pycharm or Myeditor to ide #see line 27 
matter what its should contain method execute """
class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)