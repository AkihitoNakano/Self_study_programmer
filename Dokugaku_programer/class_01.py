class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created")

or1 = Orange(10, "dark orange")
or1.weight = 100                # 変数内の値を変更
or1.color = "light orange"

print(or1.weight)
print(or1.color)
