class Minion:
    def __init__(self, a):
        self.source = a
        self.info = 1


minion1 = Minion(None)
minion2 = Minion(minion1)
print(minion1.info)
minion2.source.info = 2
print(minion1.info)
