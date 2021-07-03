class Minion:
    def __init__(self):
        self.source = self


minion = Minion()
print(minion.source)
print(minion.source.source)
