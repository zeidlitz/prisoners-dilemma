from enum import Enum


class Choice(Enum):
    COOPERATE = "COOPERATE"
    DETER = "DETER"


class Prisoner:
    def __init__(self):
        self.match_history = {}
        self.score = 0

    def choose(self):
        pass
