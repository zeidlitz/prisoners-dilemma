import random
import globals
from enum import Enum


class Choice(Enum):
    COOPERATE = "COOPERATE"
    DETER = "DETER"


class Prisoner:
    def __init__(self, strategy):
        self.strategy = strategy
        self.match_history = {}
        self.counter = 0
        self.score = 0

    def choose(self):
        if (self.strategy == "kind"):
            return Choice.COOPERATE

        if (self.strategy == "mean"):
            return Choice.DETER

        if (self.strategy == "anti-sneaky"):
            if random.randint(1, 3) == 1:
                return Choice.COOPERATE
            else:
                return Choice.DETER

        if (self.strategy == "sneaky"):
            if random.randint(1, 3) == 1:
                return Choice.DETER
            else:
                return Choice.COOPERATE

        if (self.strategy == "fiddyfiddy"):
            if random.choice([True, False]):
                return Choice.DETER
            else:
                return Choice.COOPERATE

        if (self.strategy == "backstabber"):
            if (self.counter == 10):
                self.counter = 0
            if self.counter < (globals.numberOfMatches * 0.7):
                self.counter += 1
                return "share"
            else:
                self.counter += 1
                return "take"
