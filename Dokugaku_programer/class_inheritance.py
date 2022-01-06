class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print(f"{self.width} by {self.len}")

class Squre(Shape):
    pass

a_square = Squre(20,20)
a_square.print_size()
