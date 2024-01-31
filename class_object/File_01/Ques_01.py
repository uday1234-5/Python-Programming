class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print('-'*80)
        print(f"Area of rectengle having length({self.length}cm) and breadth({self.breadth}cm) = {self.length*self.breadth} sq.cm")
        print('-'*80)
    def perimeter(self):
        print(f"Perimeter of rectengle having length({self.length}cm) and breadth({self.breadth}cm) = {2*(self.length+self.breadth)} cm")
        print('-'*80)
        
l = float(input("Enter length of rectangle : "))
b = float(input("Enter length of rectangle : "))
rec = rectangle(1,b)
rec.area()
rec.perimeter()