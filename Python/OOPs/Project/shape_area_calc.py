class shape:
    
    def square(self):
        side = eval(input("Enter the side of square : "))
        print('*'*50)
        print(f"Area of square having side({side}) = {side**2}")
        print(f"Perimeter of square having side({side}) = {side*4}")
        print('*'*50)
        
    def rectangle(self):
        print('*'*50)
        length = eval(input("Enter the length of rectangle : "))
        breadth = eval(input("Enter the breadth of rectangle : "))
        print('*'*50)
        print(f"Area of rectangle having length({length}) and breadth({breadth}) = {length*breadth}")
        print(f"Perimeter of rectangle having length({length}) and breadth({breadth}) = {2*(length+breadth)}")
        print('*'*50)
        
    def circle(self):
        radius = float(input("Enter radius of circle : "))
        print('*'*50)
        print(f"Area of circle having radius({radius}) = {3.14 * radius**2}")
        print(f"Circumference of circle having radius({radius}) = {3.14 * radius*2}")
        print('*'*50)
area = shape()
area.square()
area.rectangle()
area.circle()

        