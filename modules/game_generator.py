import random
import copy
from modules.settings import Settings, States
from modules.units import unit


class GameGenerator:

    def __init__(self):
        self.teams = None
        self.team_values = None

    def main(self):
        self.reset()
        self.generate_team("left")
        self.generate_team("right")

        return self.teams["left"], self.teams["right"]

    def reset(self):
        self.teams = {"left": [], "right": []}
        self.team_values = {"left": 0, "right": 0}

    def generate_team(self, team):
        col = {"left": 0, "right": 14}
        team_id = {"left": 1, "right": 2}

        for row in [1, 3, 5, 7, 9]:
            name = self.generate_unit()
            value = self.generate_unit_value(team)

            character = unit(name, row, col[team], 0, team_id[team])
            character.count = self.get_unit_count(value, character.ai)

            self.teams[team].append(character)
        print(f"{team} team value is {self.team_values[team]}")

    @staticmethod
    def generate_unit():
        possible_units = ["nimph", "oceanid", "pkman", "halbd", "pixie", "sprit", "trogl", "itrog", "gnoll", "gnolm",
                          "imp", "famil", "skele", "wskel", "dwarf", "bdwar", "gobli", "hgobl", "grema", "gremm"]
        return possible_units[random.randint(0, len(possible_units) - 1)]

    def generate_unit_value(self, team):
        value = random.randint(750, 2000)
        self.team_values[team] += value
        return value

    @staticmethod
    def get_unit_count(value, ai):
        return int(value / ai)

