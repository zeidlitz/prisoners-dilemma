import globals
from Tournament import Tournament
from Benevolent import Benevolent
from Greedy import Greedy
from Gambler import Gambler
from Backstabber import Backstabber

if __name__ == "__main__":

    participants = [
        Benevolent("Kind-Albert"),
        Benevolent("Kind-Simon"),
        Greedy("Greedy-Frank"),
        Backstabber("Backstabbing-Abby"),
        Gambler("Gambling-Sarah")
    ]

    t = Tournament(globals.numberOfMatches, participants)
    t.run()
