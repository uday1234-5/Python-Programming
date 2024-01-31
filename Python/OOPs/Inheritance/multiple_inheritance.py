class A:
    def __init__(self) -> None:
        self.a = 10
    def disp(self):
        return "This is an attribute in class A inherited by class C"
class B:
    def __init__(self) -> None:
        self.b = 100
    def disp2(self):
        return "This is an attribute in class B inherited by class C"
        
class C(A,B):
    # def __init__(self) -> None:
    #     A.__init__(self) #This will inherit instance variable "a" from class A
    #     B.__init__(self) #This will inherit instance variable "b" from class B
    #     # super().__init__() #This inherits __init__ from the parent class i.e. that class which is inherited
    #     self.c = 1000
        pass
r1 = C()
print(r1.__dict__)
print(r1.disp())
print(r1.disp2())