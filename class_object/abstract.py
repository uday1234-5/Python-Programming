from abc import ABC,abstractmethod
class Rect(ABC):
    @abstractmethod
    def area(self,l,b):
        return l*b
    @abstractmethod
    def perimeter(self,l,b):
        return 2*(l+b)
class Rectangle(Rect):
    def area(self,l,b):
        return super().area(l,b)
    def perimeter(self,l,b):
        return super().perimeter(l,b)
obj = Rectangle()
print(obj.area(3,8))
print(obj.perimeter(3,8))