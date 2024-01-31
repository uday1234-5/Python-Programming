class person:
    name = "Uday Kushwah "
    age = 18
    university = "GLA University "
    def info(self):
        print(f"My Name is {self.name} and I am {self.age} years old and currently pursuing B-Tech from {self.university}")
obj = person()  
obj.info()   # person().info() 