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
        Greedy("Greedy-Frank"),
        T4T("T4T-Bob"),
        # T4T("T4T-Richard"),
        # Benevolent("Kind-Albert"),
        # Benevolent("Kind-Bobby"),
        # Benevolent("Kind-Robert"),
        # Benevolent("Kind-Sam"),
        # Benevolent("Kind-Simon"),
        # Greedy("Greedy-Harold"),
        # T4T("T4T-Claire"),
        # Backstabber("Backstabbing-Abe"),
        # Gambler("Gambling-Sarah"),
        # Backstabber("Backstabbing-Abby"),
        # Gambler("Gambling-Katy")
    ]

    t = Tournament(globals.numberOfMatches, participants, args.debug)
    t.run()
