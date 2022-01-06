class Square:
    def __init__(self, edge_len):
        self.edge_len = edge_len

    def calculate_perimeter(self):
        return 4*self.edge_len

    def add_size(self, add_value):
        self.edge_len += add_value

    def change_size(self, size):
        self.edge_len = size

square1 = Square(10)
square1.add_size(10)
square1.change_size(100)
print(square1.calculate_perimeter())
