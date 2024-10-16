from Prisoner import Prisoner, Choice


class Benevolent(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose(self):
        return Choice.COOPERATE
