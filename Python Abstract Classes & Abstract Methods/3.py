from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle area:", math.pi * self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle area:", self.length * self.width)


circle = Circle(5)
rectangle = Rectangle(10, 5)

circle.area()
rectangle.area()