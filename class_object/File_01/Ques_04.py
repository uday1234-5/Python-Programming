class Animal:
    def __init__(self,name,species,age):
        self.name = name
        self.age = age
        self.species = species
    def display_details(self):
        return f"""
    Name   : {self.name}
    Age    : {self.age}
    Species: {self.species}
    """
    
class Lion(Animal):
    def __init__(self,name,species,age,weight):
        super().__init__(self,name,species,age)
        self.weight = weight
        print()
    