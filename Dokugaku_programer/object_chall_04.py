class Rider:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__(self, hname, owner):
        self.hname = hname
        self.owner = owner

rider_take = Rider("Take Yutaka")
horse = Horse("deep impact",rider_take )

print(horse.owner.name)
