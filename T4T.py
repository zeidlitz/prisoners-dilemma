import globals
from Prisoner import Prisoner, Choice


class T4T(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.opponent
        self.numberOfMatches = globals.numberOfMatches

    def choose(self, opponent):
        return Choice.COOPERATE
