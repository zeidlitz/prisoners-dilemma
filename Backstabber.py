import globals
from Prisoner import Prisoner, Choice


class Backstabber(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.counter = 0
        self.ratio = 0.7  # This is saying: we COOPERATE 70% of the times and then DETER the rest of the round
        self.numberOfMatches = globals.numberOfMatches

    '''
    The backstabber will COOPERATE a set number of times and then only DETER
    '''

    def choose(self):
        self.counter += 1
        if (self.counter == self.numberOfMatches):
            self.counter = 0
        if (self.counter < (self.numberOfMatches * self.ratio)):
            return Choice.COOPERATE
        else:
            return Choice.DETER
