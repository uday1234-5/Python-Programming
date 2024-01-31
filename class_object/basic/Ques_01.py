class demo:
    x = "abc"     #class variable
    y = 5
    def __init__(self,name,color):
        self.name = name               #instance variable
        self.color = color
obj1 = demo("Uday","Yellow")
obj2 = demo("Rohit","Red")

print("Object 1 details")
print(obj1.x)
print(obj1.name)
print(obj1.color)

print("Object 2 details")
print(obj2.y)
print(obj2.name)
print(obj2.color)
print("****************")
print(__name__)