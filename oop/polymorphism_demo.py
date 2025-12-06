import math

class Shape:
    def area():
        return "Area of the shape"


class Rectangle:
    def area(self, width, height):
        self.width = width
        self.height = height
        return width * height
    

class Circle:
    def area(self, radus):
        self.radus = radus
        return math.pi * (radus ** 2)


