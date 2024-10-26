import random
from Prisoner import Prisoner, Choice


class Gambler(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose(self, opponent):
        if random.choice([True, False]):
            choice = Choice.COOPERATE
            self.update_choice_history(opponent, choice)
            return choice
        else:
            choice = Choice.DETER
            self.update_choice_history(opponent, choice)
            return choice
