class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Squre(Shape):
    def __init__(self, edge_len):
        self.edge_len = edge_len
    def calculate_perimeter(self):
        return 4*self.edge_len

    def what_am_i(self):
        super().what_am_i()
        print('I am a square.')

square1= Squre(10)
# print(square1.calculate_perimeter())
square1.what_am_i()
