import random
from Prisoner import Prisoner, Choice


class Gambler(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose(self):
        if random.choice([True, False]):
            return Choice.COOPERATE
        else:
            return Choice.DETER
