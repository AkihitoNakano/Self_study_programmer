import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pow(self.radius, 2)*math.pi

circle1 = Circle(5)
print(circle1.area())
