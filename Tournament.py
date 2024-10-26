from tabulate import tabulate
import pdb


class Tournament:
    def __init__(self, numberOfMatches, participants, debug=False):
        self.debug = debug
        self.numberOfMatches = numberOfMatches
        self.participants = participants

    '''
    Singular: Award score to only p0
    '''

    def give_score(self, score_gained, p0, p1):
        p0.match_history[p1.name] += score_gained
        p0.score += score_gained

    '''
    Plural: Award score to both p0 and p1
    '''

    def give_scores(self, score_gained, p0, p1):
        p0.match_history[p1.name] += score_gained
        p0.score += score_gained

        p1.match_history[p0.name] += score_gained
        p1.score += score_gained

    def end_game(self, participants):
        print()
        table_data = []
        max_score = 0
        winner = None
        row = ["name", "score", "history"]
        table_data.append(row)
        for p in participants:
            if (p.score > max_score):
                max_score = p.score
                winner = p.name
            row = [p.name, p.score, p.match_history]
            table_data.append(row)
        # print(tabulate(table_data, headers="firstrow"))
        print("\nWinner : ", winner)

    def run(self):
        matches = []

        participants = self.participants

        for bot in participants:
            bot.match_history = {p.name: 0 for p in participants if p != bot}

        for i in range(len(participants)):
            for j in range(i + 1, len(participants)):
                matches.append((participants[i], participants[j]))

        for m in matches:
            p0_choises = []
            p1_choises = []
            for x in range(self.numberOfMatches):
                p0 = m[0]
                p1 = m[1]

                p0_choise = p0.choose(p1).name
                p1_choise = p1.choose(p0).name
                p0_choises.append(p0_choise)
                p1_choises.append(p1_choise)

                if p0_choise == "COOPERATE" and p1_choise == "COOPERATE":
                    score_gained = 3
                    self.give_scores(score_gained, p0, p1)

                if p0_choise == "DETER" and p1_choise == "DETER":
                    score_gained = 1
                    self.give_scores(score_gained, p0, p1)

                if p0_choise == "COOPERATE" and p1_choise == "DETER":
                    score_gained = 5
                    self.give_score(score_gained, p1, p0)

                if p0_choise == "DETER" and p1_choise == "COOPERATE":
                    score_gained = 5
                    self.give_score(score_gained, p0, p1)

            if self.debug:
                r0 = ['O' if x == "COOPERATE" else 'X' for x in p0_choises]
                r1 = ['O' if x == "COOPERATE" else 'X' for x in p1_choises]

                print()  # Sepperator for better reading
                print(r0, " : ", p0.name)
                print(r1, " : ", p1.name)
            p0_choises.clear()
            p1_choises.clear()

        self.end_game(participants)
