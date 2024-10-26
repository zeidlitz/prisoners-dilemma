from enum import Enum
import queue


class Choice(Enum):
    COOPERATE = "COOPERATE"
    DETER = "DETER"


class Prisoner:
    def __init__(self):
        self.score = 0
        self.match_history = {}
        self.choice_history = {}

    def choose(self, opponent):
        pass

    def update_choice_history(self, opponent, choice):
        if opponent not in self.choice_history:
            self.choice_history[opponent.name] = queue.LifoQueue()
        self.choice_history[opponent.name].put(choice)
