from Prisoner import Prisoner


class Tournament:
    def __init__(self, numberOfMatches):
        self.numberOfMatches = numberOfMatches

    def give_score(self, score_gained, p0, p1):
        p0.match_history[p1.strategy] += score_gained
        p0.score += score_gained

    def give_scores(self, score_gained, p0, p1):
        p0.match_history[p1.strategy] += score_gained
        p0.score += score_gained

        p1.match_history[p0.strategy] += score_gained
        p1.score += score_gained

    def end_game(self, participants):
        max_score = 0
        winner = None
        for p in participants:
            print(p.strategy, " : ", p.score, " : ", p.match_history)
            if (p.score > max_score):
                max_score = p.score
                winner = p.strategy
        print("\nWINNER : ", winner)

    def run(self):
        matches = []

        participants = [
            Prisoner("kind"),
            Prisoner("mean"),
            Prisoner("fiddyfiddy"),
            Prisoner("sneaky"),
            # Prisoner("backstabber"),
        ]

        for bot in participants:
            bot.match_history = {p.strategy: 0 for p in participants if p != bot}

        for i in range(len(participants)):
            for j in range(i + 1, len(participants)):
                matches.append((participants[i], participants[j]))

        for m in matches:
            for x in range(self.numberOfMatches):
                p0 = m[0]
                p1 = m[1]

                p0_choise = p0.choose().name
                p1_choise = p1.choose().name

                if p0_choise == "COOPERATE" and p1_choise == "COOPERATE":
                    score_gained = 3
                    self.give_score(score_gained, p0, p1)

                if p0_choise == "DETER" and p1_choise == "DETER":
                    score_gained = 1
                    self.give_scores(score_gained, p0, p1)

                if p0_choise == "COOPERATE" and p1_choise == "DETER":
                    score_gained = 5
                    self.give_score(score_gained, p1, p0)

                if p0_choise == "DETER" and p1_choise == "COOPERATE":
                    score_gained = 5
                    self.give_score(score_gained, p0, p1)

        self.end_game(participants)
