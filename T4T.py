from Prisoner import Prisoner, Choice


class T4T(Prisoner):
    def __init__(self, name):
        super().__init__()
        self.name = name

    '''
    The Tit-for-Tat strategy starts by cooperating and then mirrors the opponent's last move. It uses the choice history for immediate response to the opponent's last move.
    '''

    def choose(self, opponent):
        # If no previous choice, start with cooperate
        if opponent.name not in self.choice_history or self.choice_history[opponent.name].empty():
            choice = Choice.COOPERATE
        else:
            # Get the opponent's last choice from choice history
            choice = opponent.choice_history[self.name].get()

        # Update choice history and memory
        self.update_choice_history(opponent, choice)
        self.update_memory(opponent, choice)
        return choice