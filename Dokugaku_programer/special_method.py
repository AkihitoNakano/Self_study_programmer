class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # インスタンスをprint関数に渡すとPythonはobjectクラスから継承した__repr__を呼び出す
        return self.name



lion = Lion("Dilbert")
print(lion)
