class Shape:
    def area(self):
        print("Shape area")
class Rectangle(Shape):
    def area(self):
        print("Rectangle area = length × width")
class Circle(Shape):
    def area(self):
        print("Circle area = π × radius × radius")
class Triangle(Shape):
    def area(self):
        print("Triangle area = 1/2 × base × height")
r = Rectangle()
c = Circle()
t = Triangle()
r.area()
c.area()
t.area()