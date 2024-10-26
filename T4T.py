import globals
import pdb
from Prisoner import Prisoner, Choice


class T4T(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.numberOfMatches = globals.numberOfMatches

    '''
    The Tit For Tat strategy will be cooperative unless someone have detered them before. The base case if we have not met the opponent before is to cooperate. Else we will pick the choice they did to us previously.
    '''

    def choose(self, opponent):
        try:
            # pdb.set_trace()
            opponents_choice_history = opponent.choice_history[self.name]
            choice = opponents_choice_history.get()
        except KeyError:
            choice = Choice.COOPERATE
        return choice
