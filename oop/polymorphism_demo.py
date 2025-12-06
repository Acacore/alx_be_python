import math

class Shape:
    def area(self):
        return "Area of the shape"


class Rectangle(Shape):
    def area(self, width, height):
        self.width = width
        self.height = height
        return width * height
    

class Circle(Shape):
    def area(self, radus):
        self.radus = radus
        return math.pi * (radus ** 2)


