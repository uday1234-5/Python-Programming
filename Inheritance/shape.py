"""
Q1. Class Inheritance:
Create a base class Shape with methods area and perimeter. Create two
derived classes, Rectangle and Circle. Implement the necessary methods in each derived class."""
# import math
from math import pi
class shape:
    # def __init__(self,radius,length,breadth):
    #     self.radius = radius
    def calc_area_perimeter_circle(self,radius):
        if radius > 0:
            print('*'*80)
            print(f"Area of circle having radius({radius}cm) = {(pi*(radius**2)):.3f} sq.cm")
            print(f"Circumference of circle having radius({radius}cm) = {(pi*radius*2):.3f} cm")
            print('*'*80)
    def calc_area_perimeter_rectangle(self,length,breadth):
        if length >0 and breadth > 0:
            print('*'*80)
            print(f"Area of rectengle having length({length}cm) and breadth({breadth}cm) = {length*breadth} sq.cm")
            print(f"Perimeter of rectengle having length({length}cm) and breadth({breadth}cm) = {2*(length+breadth)} cm")
            print('*'*80)
class circle(shape):
    pass
    