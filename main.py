import random


class Bot:
    def __init__(self, strategy):
        self.strategy = strategy
        self.fooled = False
        self.match_history = {}
        self.score = 0
        self.counter = 0

    def draw(self):
        if (self.strategy == "kind"):
            return "share"

        if (self.strategy == "mean"):
            return "take"

        if (self.strategy == "anti-sneaky"):
            if random.randint(1, 3) == 1:
                return "share"
            else:
                return "take"

        if (self.strategy == "sneaky"):
            if random.randint(1, 3) == 1:
                return "take"
            else:
                return "share"

        if (self.strategy == "fiddyfiddy"):
            if random.choice([True, False]):
                return "take"
            else:
                return "share"

        if (self.strategy == "backstabber"):
            if (self.counter == 10):
                self.counter = 0
            if self.counter < (numberOfMatches * 0.7):
                self.counter += 1
                return "share"
            else:
                self.counter += 1
                return "take"

        if (self.strategy == "hero"):
            if (self.fooled):
                self.fooled = False
                return "take"
            return "share"

        if (self.strategy == "anti-hero"):
            if (self.fooled):
                self.fooled = False
                return "share"
            return "take"


def give_score(score_gained, player0, player1):
    player0.match_history[player1.strategy] += score_gained
    player0.score += score_gained


def give_scores(score_gained, player0, player1):
    player0.match_history[player1.strategy] += score_gained
    player0.score += score_gained

    player1.match_history[player0.strategy] += score_gained
    player1.score += score_gained


def end_game(participants):
    max_score = 0
    winner = None
    for p in participants:
        if (p.score > max_score):
            max_score = p.score
            winner = p.strategy

    print("\nWINNER : ", winner)


if __name__ == "__main__":

    numberOfMatches = 10
    matches = []

    participants = [
        Bot("kind"),
        Bot("mean"),
        Bot("fiddyfiddy"),
        Bot("sneaky"),
        Bot("anti-sneaky"),
        Bot("hero"),
        Bot("backstabber")
    ]

    for bot in participants:
        bot.match_history = {p.strategy: 0 for p in participants if p != bot}

    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):
            matches.append((participants[i], participants[j]))

    for m in matches:
        for x in range(numberOfMatches):
            player0 = m[0]
            player1 = m[1]
            player0_action = player0.draw()
            player1_action = player1.draw()

            if player0_action == "take" and player1_action == "take":
                score_gained = 1
                give_score(score_gained, player0, player1)

            if player0_action == "share" and player1_action == "share":
                score_gained = 3
                give_scores(score_gained, player0, player1)

            if player0_action == "take" and player1_action == "share":
                score_gained = 5
                give_score(score_gained, player0, player1)

            if player0_action == "share" and player1_action == "take":
                score_gained = 5
                give_score(score_gained, player1, player0)

    end_game(participants)
