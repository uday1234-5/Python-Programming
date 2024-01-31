import math
class circle:
    def __init__(self,radius):
        self.radius = radius
    def Ar_circle(self):
        print('*'*80)
        print(f"Area of circle having radius({self.radius}cm) = {(math.pi*(self.radius**2)):.3f} sq.cm")
        # print('*'*80)
class cylinder(circle):
    def __init__(self,radius,height):
        circle.__init__(self,radius)
        self.height = height
    def Ar_cylinder(self):
        print(f"Area of cylinder having radius({self.radius}cm) and height({self.height}cm) = {(math.pi*(self.radius**2)*self.height):.3f} cubic cm")
        # print('*'*80)
class cone(circle):
    def __init__(self,radius,slant_height,height):
        circle.__init__(self,radius)
        self.slant_height = slant_height
        self.height = height
    def Ar_cone(self):
        print(f"Area of cone having radius({self.radius}cm), slant height({self.slant_height}cm) and height({self.height}cm) = {(math.pi*self.radius*(self.height+self.slant_height)):.3f} cubic cm")
        print('*'*80)
# r1 = circle(7)
# r1.Ar_circle()

c1 = cylinder(7,5)
c1.Ar_circle()
c1.Ar_cylinder()

co1 = cone(3,5,4)
co1.Ar_cone()
