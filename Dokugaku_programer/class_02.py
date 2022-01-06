class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

or1 = Orange(100, "dark orange")
or2 = Orange(4,"light orange")
or3 = Orange(30, "yellow")

print(or2.color)
print(or2.weight)
print(or3.color)
print(or3.weight)
