class Triangle:
    def __init__(self,bottom, height):
        self.bottom = bottom
        self.height = height

    def area(self):
        return (self.bottom* self.height)/2

tri_1 = Triangle(10,20)
print(tri_1.area())
