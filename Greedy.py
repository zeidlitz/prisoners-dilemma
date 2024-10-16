from Prisoner import Prisoner, Choice


class Greedy(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose(self):
        return Choice.DETER
