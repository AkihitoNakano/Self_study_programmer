class Hexagon:
    def __init__(self, radius):
        self.radius = radius

    def circulate_perimeter(self):
        return self.radius*6

hex1 = Hexagon(6)
print(hex1.circulate_perimeter())
