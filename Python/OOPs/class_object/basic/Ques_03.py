"""Write a program to demonstrate the use of self with an instance variable to solve the problem ofbvariable hiding."""
class Demo:
    x = 9
    def __init__(self,x):
       self.x = 25
        # pass
    def display(self,x):
        x = 30
        print(x)
        print(self.x)
        print(Demo.x)
d = Demo(5)
d.display(50)

