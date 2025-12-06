import math

class Shape:
    def area(self):
        return "Area of the shape"


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    

class Circle(Shape):
    def __init__(self, radius):
        self.radus = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)


