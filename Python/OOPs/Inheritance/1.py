class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show_detail(self):
        print(f"Name is {self.name}.\nAge is {self.age}")
class child(Parent):
    pass
p1 = Parent("kamal",89)
p1.show_detail()

c1 = child('Uday',18)
c1.show_detail()