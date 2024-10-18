import globals
import argparse
from Tournament import Tournament
from Benevolent import Benevolent
from Greedy import Greedy
from Gambler import Gambler
from T4T import T4T
from Backstabber import Backstabber

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', type=bool, default=False, help='Enable or disable debug mode')
    args = parser.parse_args()

    participants = [
        Benevolent("Kind-Albert"),
        Benevolent("Kind-Simon"),
        Greedy("Greedy-Frank"),
        Backstabber("Backstabbing-Abby"),
        T4T("T4T-Claire"),
        Gambler("Gambling-Sarah")
    ]
    t = Tournament(globals.numberOfMatches, participants, args.debug)
    t.run()
