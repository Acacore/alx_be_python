import math

class Shape:
    def area(self):
        return "Area of the shape"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, raduis):
        self.radus = raduis
        
    def area(self):
        return math.pi * (self.raduis ** 2)


