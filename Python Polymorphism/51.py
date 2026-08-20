class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
class Rectangle(Shape):
    def area(self):
        return 5 * 4
class Triangle(Shape):
    def area(self):
        return 0.5 * 4 * 5
print(Circle().area())
print(Rectangle().area())
print(Triangle().area())