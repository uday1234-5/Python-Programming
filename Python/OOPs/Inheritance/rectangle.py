class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def Ar_rect(self):
        print('*'*80)
        print(f"Area of rectengle having length({self.length}cm) and breadth({self.breadth}cm) = {self.length*self.breadth} sq.cm")
        print('*'*80)
class cuboid(rectangle):
    def __init__(self,length,breadth,height):
        rectangle.__init__(self,length, breadth)
        self.height = height
    def Ar_cuboid(self):
        print(f"Area of cuboid having length({self.length}cm), breadth({self.breadth}cm) and height({self.height}cm) = {self.length*self.breadth*self.height} cubic cm")
        print('*'*80)


c1 = cuboid(3,4,5)
c1.Ar_cuboid()
c1.Ar_rect()