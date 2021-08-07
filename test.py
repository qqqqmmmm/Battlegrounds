class Minion:
    def __init__(self):
        c = {1, 2, 3}
        self.a = c
        self.b = c.union(set())


minion = Minion()
print(minion.a is minion.b)
print(minion.a)
print(minion.b)
