#Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, widht, hight):
        self.width = widht
        self.hight = hight

    def area(self):
        return self.width * self.hight
    
class Triangle(Shape):
    def __init__(self, hypo, base, perp):
        self.hypo = hypo
        self.base = base
        self.perp = perp

ans = Rectangle(5, 5)
ans = Triangle(12, 6, 6)
print("Area of rectangle = ",ans.area())
print("Area of triangle = ",ans.__init__())