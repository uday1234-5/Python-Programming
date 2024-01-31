class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show_detail(self):
        print(f"Name is {self.name}.\nAge is {self.age}")
class child(Parent):
    def __init__(self,name,age,birth_year):
        Parent.__init__(self,name,age)
        self.birth_year = birth_year
    def show_detail(self):
        print(f"Name is {self.name}.\nAge is {self.age}\nBirth Year is {self.birth_year}")

p1 = Parent("kamal",89)
p1.show_detail()

c1 = child('Uday',18,2006)
c1.show_detail()
