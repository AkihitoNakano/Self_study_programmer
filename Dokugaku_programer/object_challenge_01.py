import math

# 正三角形の場合
class Rectangle:
    def __init__(self, radius):
        self.radius = radius

    def area_length(self):
        # 正弦定理
        # C** = a** + b** - 2ab*cosθ
        c = pow(self.radius,2)*2 - 2*(self.radius)*math.cos(math.radians(120))
        return math.sqrt(c)

    def total_area_len(self):
        return 2*(self.radius) + self.area_length()

# rec1 = Rectangle(10)
# print(rec1.total_area_len())


# 正三角形以外で2辺とその間の角がわかっている場合
class Rectangle2:
    def __init__(self,edge_a, edge_b, degree):
        self.edge_a = edge_a
        self.edge_b = edge_b
        self.degree = degree

    def area_length02(self):
        c2 = pow(self.edge_a, 2) + pow(self.edge_b, 2) -2*(self.edge_a)*(self.edge_b)*math.cos(math.radians(self.degree))
        return math.sqrt(c2)

    def total_area_len02(self):
        return self.edge_a + self.edge_b + self.area_length02()

# rec2 = Rectangle2(5,10,60)
# print(rec2.total_area_len02())

class Square:
    def __init__(self, edge_len):
        self.edge_len = edge_len

    def calculate_perimeter(self):
        return 4*self.edge_len

square1 = Square(5)
print(square1.calculate_perimeter())
