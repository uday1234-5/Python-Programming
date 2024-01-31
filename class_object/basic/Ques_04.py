class Demo:
    name = ''
    age = ''
    def display(self):
        # name = input("Enter name : ")
        name = "Uday"
        print(name)
        # age = int(input("Enter age : "))
        age = "19"
        print(age)
d = Demo()
d.display()
# print(len(dir(Demo)))  
# print((dir(Demo)))
print(Demo.__dict__)
print(Demo.__doc__)
print(Demo.__module__) #__main__
print(Demo.__class__)