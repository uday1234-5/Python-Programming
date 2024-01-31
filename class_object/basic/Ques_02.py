class dog:
    animal = "Dog"
    def __init__(self,breed):
        self.breed = breed
    def setcolor(self,color):
        self.color = color
    def getcolor(self,color):
        return self.color
d1 = dog("abc")
d1.setcolor("Brown")

d2 = dog("xyz")
d2.setcolor("Black")

print(d1.getcolor)
print(d2.getcolor)
