class Number :
    def __init_(self):
        self.num = int(input("Enter number --> "))
    def square(self):
        print("The Square of is ",self.num**2)
    def cube(self):
        print("The Cube of  is ",self.num**3)
sq = Number()
sq.square()
# print(sq.num)

cb = Number()
cb.cube()
# print(cb.num)