class Square:
    square_list = []
    def __init__(self, w):
        self.square_list.append(self)
        self.width = w

    def __repr__(self):
        return f"by {self.width} by {self.width} by {self.width} by {self.width}"

s1 = Square(10)
s2 = Square(5)
print(s2)
